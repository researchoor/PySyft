# future
from __future__ import annotations

# stdlib
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from typing import Tuple
from typing import Union

# third party
import numpy as np

# syft absolute
import syft as sy

# relative
from ..common.serde.capnp import CapnpModule
from ..common.serde.capnp import get_capnp_schema
from ..common.serde.capnp import serde_magic_header
from ..common.serde.serializable import serializable
from .broadcastable import is_broadcastable
from .passthrough import is_acceptable_simple_type  # type: ignore
from .smpc.utils import get_shape

if TYPE_CHECKING:
    # relative
    from .autodp.phi_tensor import PhiTensor

func_dict = {
    "np.add": np.add,
    "np.subtract": np.subtract,
    "np.multiply": np.multiply,
    "np.matmul": np.matmul,
    "np.equal": np.equal,
    "np.not_equal": np.not_equal,
    "np.less_equal": np.less_equal,
    "np.greater_equal": np.greater_equal,
    "np.less": np.less,
    "np.greater": np.greater,
    "np.sum": np.sum,
}


@serializable(capnp_bytes=True)
class lazyrepeatarray:
    """
    When data is repeated along one or more dimensions, store it using lazyrepeatarray
    so that you can save on RAM and CPU when computing with it. Think like the opposite
    of np.broadcast, repeated values along an axis are collapsed but the .shape
    attribute of the higher dimensional projection is retained for operations.
    """

    __attr_allowlist__ = ["data", "shape"]

    def __init__(
        self,
        data: np.ndarray,
        shape: Tuple[int, ...],
        transforms: Optional[List] = None,
    ) -> None:
        """
        data: the raw data values without repeats
        shape: the shape of 'data' if repeats were included
        """

        # NOTE: all additional arguments are assumed to be broadcast if dims are shorter
        # than that of data. Example: if data.shape == (2,3,4) and
        # min_vals.shape == (2,3), then it's assumed that the full min_vals.shape is
        # actually (2,3,4) where the last dim is simply copied.
        # Example2: if data.shape == (2,3,4) and min_vals.shape == (2,1,4), then the
        # middle dimension is supposed to be copied to be min_vals.shape == (2,3,4)
        # if necessary. This is just to keep the memory footprint (and computation)
        # as small as possible.

        if isinstance(data, (bool, int, float)):
            data = np.array(data)

        # verify broadcasting works on shapes
        np.broadcast_shapes(data.shape, shape)

        if transforms is None:
            self.transforms = []
        else:
            self.transforms = transforms

        self.data = data
        self.shape = shape
        self._shape = self.shape

    def _object2bytes(self) -> bytes:
        schema = get_capnp_schema(schema_file="lazy_repeat_array.capnp")

        lazy_repeat_array_struct: CapnpModule = schema.LazyRepeatArray  # type: ignore
        lazy_repeat_array_msg = lazy_repeat_array_struct.new_message()

        lazy_repeat_array_msg.magicHeader = serde_magic_header(type(self))

        lazy_repeat_array_msg.data = sy.serialize(self.data, to_bytes=True)
        lazy_repeat_array_msg.shape = sy.serialize(self.shape, to_bytes=True)
        lazy_repeat_array_msg.transforms = sy.serialize(self.transforms, to_bytes=True)

        return lazy_repeat_array_msg.to_bytes_packed()

    @staticmethod
    def _bytes2object(buf: bytes) -> lazyrepeatarray:
        schema = get_capnp_schema(schema_file="lazy_repeat_array.capnp")
        lazy_repeat_array_struct: CapnpModule = schema.LazyRepeatArray  # type: ignore
        MAX_TRAVERSAL_LIMIT = 2**64 - 1

        lazy_repeat_array_msg = lazy_repeat_array_struct.from_bytes_packed(
            buf, traversal_limit_in_words=MAX_TRAVERSAL_LIMIT
        )

        data = sy.deserialize(lazy_repeat_array_msg.data, from_bytes=True)
        shape = sy.deserialize(lazy_repeat_array_msg.shape, from_bytes=True)
        transforms = sy.deserialize(lazy_repeat_array_msg.transforms, from_bytes=True)

        return lazyrepeatarray(
            data=data,
            shape=shape,
            transforms=transforms,
        )

    def __add__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data + other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.add", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.add", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __sub__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data - other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.subtract", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.subtract", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __mul__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data * other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.multiply", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.multiply", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __matmul__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            raise Exception
        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if len(self.shape) != 2 or len(other.shape) != 2:
                raise Exception("Matmul only valid for 2D arrays")

            if self.shape[-1] != other.shape[0]:
                raise Exception(
                    "Cannot matrix multiply tensors with different shapes: {self.shape} and {other.shape}"
                )
            else:
                self.shape = (self.shape[0], other.shape[-1])
                if isinstance(other, lazyrepeatarray):
                    self.add_op(function="np.matmul", args=other)
                elif isinstance(other, np.ndarray):
                    self.add_op(function="np.matmul", args=other)
                return self

    def __eq__(self, other: Any) -> lazyrepeatarray:  # type: ignore
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data == other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.equal", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.equal", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __ne__(self, other: Any) -> lazyrepeatarray:  # type: ignore
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data != other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.not_equal", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.not_equal", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __le__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data <= other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.less_equal", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.less_equal", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __ge__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data >= other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.greater_equal", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.greater_equal", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __lt__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data < other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.less", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.less", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __gt__(self, other: Any) -> lazyrepeatarray:
        if isinstance(other, (int, np.integer, float, np.floating)):
            return lazyrepeatarray(data=(self.data > other), shape=self.shape)

        elif isinstance(other, (np.ndarray, lazyrepeatarray)):  # type: ignore
            if not is_broadcastable(self.shape, other.shape):
                raise Exception(
                    f"Cannot broadcast arrays with shapes: {self.shape} & {other.shape}"
                )
            self.shape = np.broadcast_shapes(self.shape, other.shape)
            if isinstance(other, lazyrepeatarray):
                self.add_op(function="np.greater", args=other.data)
            elif isinstance(other, np.ndarray):
                self.add_op(function="np.greater", args=other)
            return self

        else:
            raise Exception(f"not sure how to do this yet: {type(other)}")

    def __neg__(self) -> lazyrepeatarray:
        self.data *= -1
        return self

    def __rmatmul__(self, other: Any) -> lazyrepeatarray:
        if is_acceptable_simple_type(other):
            self.shape = get_shape("__matmul__", other.shape, self.shape)

            if other.size == 1:
                self.add_op(function="np.rmatmul", args=other)

        if other.shape[-1] != self.shape[0]:
            raise Exception(
                "cannot matrix multiply tensors with different shapes: {self.shape} and {other.shape}"
            )

        else:
            self.shape = (other.shape[-1], self.shape[0])
            self.add_op(function="np.rmatmul", args=other)
            return self

    def __pow__(self, exponent: int) -> lazyrepeatarray:
        if exponent == 2:
            return self * self
        raise Exception("not sure how to do this yet")

    def copy(self, order: Optional[str] = "K") -> lazyrepeatarray:
        return self.__class__(data=self.data.copy(order=order), shape=self.shape)

    @property
    def size(self) -> int:
        return np.prod(self.shape)

    def sum(self, *args: Tuple[Any, ...], **kwargs: Any) -> lazyrepeatarray:
        if "axis" in kwargs and kwargs["axis"] is None:
            self.add_op(function="np.sum", args=None)
        else:
            raise Exception("not sure how to do this yet")

        return self

    def concatenate(
        self, other: lazyrepeatarray, *args: List[Any], **kwargs: Dict[str, Any]
    ) -> lazyrepeatarray:
        if not isinstance(other, lazyrepeatarray):
            raise NotImplementedError

        dummy_res = np.concatenate(
            (np.empty(self.shape), np.empty(other.shape)), *args, **kwargs
        )
        return lazyrepeatarray(data=self.data, shape=dummy_res.shape)

    @property
    def dtype(self) -> np.dtype:
        return self.data.dtype

    def astype(self, np_type: np.dtype) -> lazyrepeatarray:
        return self.__class__(self.data.astype(np_type), self.shape)

    def __repr__(self) -> str:
        return f"<lazyrepeatarray data: {self.data} -> shape: {self.shape}>"

    def __bool__(self) -> bool:
        return self.data.__bool__()

    def all(self) -> bool:
        return self.data.all()

    def any(self) -> bool:
        return self.data.any()

    def transpose(self, *args: List[Any], **kwargs: Dict[str, Any]) -> lazyrepeatarray:
        dummy_res = self.evaluate().transpose(*args, **kwargs)
        return lazyrepeatarray(
            data=self.data.transpose(*args, **kwargs), shape=dummy_res.shape
        )

    def add_op(self, function: str, selection=slice(None), args: Optional[Any] = None) -> None:  # type: ignore
        self.transforms.append((function, selection, args))

    def evaluate(self) -> np.ndarray:
        result = np.ones(self._shape) * self.data
        for func, selection, args in self.transforms:
            if func == "np.matmul":
                if isinstance(args, lazyrepeatarray):
                    args = args.evaluate()
                result = func_dict[func](result[selection], args)
            elif func == "np.rmatmul":
                if isinstance(args, lazyrepeatarray):
                    args = args.evaluate()
                func = "np.matmul"
                result = func_dict[func](args, result[selection])
            else:
                result[selection] = func_dict[func](result[selection], args)
        self.transforms = []
        return result

    # As the min and max values calculation is the same regardless of the tensor type,


# We centralize this method as baseline for calculation for min/max values
def compute_min_max(
    x_min_vals: lazyrepeatarray,
    x_max_vals: lazyrepeatarray,
    other: Union[PhiTensor, int, float, np.ndarray],
    op_str: str,
) -> Tuple[lazyrepeatarray, lazyrepeatarray]:
    min_vals: lazyrepeatarray
    max_vals: lazyrepeatarray

    if op_str in ["__add__", "__matmul__", "__rmatmul__"]:
        if is_acceptable_simple_type(other):
            min_vals = getattr(x_min_vals, op_str)(other)
            max_vals = getattr(x_max_vals, op_str)(other)
        elif hasattr(other, "min_vals") and hasattr(other, "max_vals"):
            min_vals = getattr(x_min_vals, op_str)(other.min_vals)  # type: ignore
            max_vals = getattr(x_max_vals, op_str)(other.max_vals)  # type: ignore
        else:
            raise ValueError(
                f"Not supported type for lazy repeat array computation: {type(other)}"
            )

    elif op_str in ["__sub__", "__mul__"]:
        if is_acceptable_simple_type(other):
            min_vals = getattr(x_min_vals, op_str)(other)
            max_vals = getattr(x_max_vals, op_str)(other)
        elif hasattr(other, "min_vals") and hasattr(other, "max_vals"):
            min_min = getattr(x_min_vals.data, op_str)(other.min_vals.data)  # type: ignore
            min_max = getattr(x_min_vals.data, op_str)(other.max_vals.data)  # type: ignore
            max_min = getattr(x_max_vals.data, op_str)(other.min_vals.data)  # type: ignore
            max_max = getattr(x_max_vals.data, op_str)(other.max_vals.data)  # type: ignore
            _min_vals = np.minimum.reduce([min_min, min_max, max_min, max_max])
            _max_vals = np.maximum.reduce([min_min, min_max, max_min, max_max])
            min_vals = x_min_vals.copy()
            min_vals.data = _min_vals
            max_vals = x_max_vals.copy()
            max_vals.data = _max_vals
        else:
            raise ValueError(
                f"Not supported type for lazy repeat array computation: {type(other)}"
            )

    elif op_str in ["__gt__", "__lt__", "__le__", "__ge__", "__eq__", "__ne__"]:
        min_vals = x_min_vals * 0
        max_vals = (x_max_vals * 0) + 1
    elif op_str == "sum":
        min_vals = lazyrepeatarray(data=np.array(x_min_vals.sum(axis=None)), shape=())
        max_vals = lazyrepeatarray(data=np.array(x_max_vals.sum(axis=None)), shape=())
    else:
        raise ValueError(f"Invaid Operation for LazyRepeatArray: {op_str}")

    return (min_vals, max_vals)

# stdlib
from typing import Any
from typing import List
from typing import Union

# relative
from ..exceptions import RoleNotFoundError
from ..node_table.roles import Role
from .database_manager import DatabaseManager


class RoleManager(DatabaseManager):
    schema = Role

    def __init__(self, database):
        super().__init__(schema=RoleManager.schema, db=database)

    @property
    def user_role(self):
        return self.first(name="User")

    @property
    def owner_role(self):
        return self.first(name="Owner")

    @property
    def compliance_officer_role(self):
        return self.first(name="Compliance Officer")

    @property
    def admin_role(self):
        return self.first(name="Administrator")

    def _common_roles(self) -> Any:
        return self.db.session.query(self._schema).filter_by(
            can_triage_requests=False,
            can_edit_settings=False,
            can_create_users=False,
            can_create_groups=False,
            can_upload_data=False,
            can_edit_roles=False,
            can_manage_infrastructure=False,
        )

    @property
    def common_roles(self):
        return self._common_roles().all()

    @property
    def org_roles(self):
        return self.db.session.query(self._schema).except_(self._common_roles).all()

    def first(self, **kwargs) -> Union[None, List]:
        result = super().first(**kwargs)
        if not result:
            raise RoleNotFoundError
        return result

    def query(self, **kwargs) -> Union[None, List]:
        results = super().query(**kwargs)
        if len(results) == 0:
            raise RoleNotFoundError
        return results

    def set(self, role_id, params):
        if self.contain(id=role_id):
            self.modify({"id": role_id}, params)
        else:
            raise RoleNotFoundError
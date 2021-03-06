from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER

from . import db, MenuModel
from .base import BaseModel


class RoleModel(BaseModel):
    """角色模型"""

    __tablename__ = "role"
    __table_args__ = {
        'comment': '角色表，角色可继承'
    }

    name = db.Column(String(20), nullable=False, unique=True, comment='角色名称')
    remark = db.Column(String(200), nullable=True, comment='备注')

    permissions = db.relationship(
        'PermissionModel',
        secondary='permission_role',
        primaryjoin='RoleModel.id == PermissionRoleModel.role_id',
        secondaryjoin='PermissionRoleModel.permission_id == PermissionModel.id',
        uselist=True,
        backref='roles'
    )

    parent_roles = db.relationship(
        'RoleModel',
        secondary='role_role',
        primaryjoin='RoleModel.id == RoleRoleModel.role_id',
        secondaryjoin='RoleRoleModel.parent_id == RoleModel.id',
        uselist=True
    )

    def get_permissions(self):
        permissions = []
        for parent_role in self.parent_roles:
            permissions.extend(parent_role.permissions)
        return permissions

    @staticmethod
    def get_menu(role_id):
        """get role menu"""
        role = RoleModel.query.get(role_id)
        permissions = role.get_permissions()

        menu = []
        # Step1 add common menu
        menu.extend(MenuModel.get_common_menu())

        # Step2 add permission menu (remove duplicates)
        for permission in permissions:
            for item in permission.get_menus():
                if item['id'] not in [item['id'] for item in menu]:
                    menu.append(item)

        # Step3 order
        menu.sort(key=lambda x: x['order'])
        return menu

    def __repr__(self):
        return f'<RoleModel {self.id}>'


class RoleRoleModel(BaseModel):
    """角色角色多对多模型"""

    __tablename__ = "role_role"
    __table_args__ = {
        'comment': '角色角色多对多'
    }

    role_id = db.Column(INTEGER(unsigned=True), comment='角色ID')
    parent_id = db.Column(INTEGER(unsigned=True), comment='父级角色ID')


class RoleUserModel(BaseModel):
    """角色用户多对多模型"""

    __tablename__ = 'role_user'
    __table_args__ = {
        'comment': '角色用户多对多表'
    }

    role_id = db.Column(INTEGER(unsigned=True), comment='角色ID')
    user_id = db.Column(INTEGER(unsigned=True), comment='用户ID')

    def __repr__(self):
        return f'<RoleUserModel {self.id}>'

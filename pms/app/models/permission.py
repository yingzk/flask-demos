from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER

from . import db
from .base import BaseModel


class PermissionModel(BaseModel):
    """权限模型"""

    __tablename__ = 'permission'
    __table_args__ = {
        'comment': '权限表'
    }

    name = db.Column(String(20), nullable=False, unique=True, comment='权限名')
    remark = db.Column(String(200), nullable=True, comment='备注')

    def __repr__(self):
        return f'<PermissionModel {self.id}>'


class PermissionRoleModel(BaseModel):
    """权限角色多对多模型"""

    __tablename__ = 'permission_role'
    __table_args__ = {
        'comment': '权限角色多对多表'
    }

    permission_id = db.Column(INTEGER(unsigned=True), comment='权限ID')
    role_id = db.Column(INTEGER(unsigned=True), comment='角色ID')

    def __repr__(self):
        return f'<PermissionRoleModel {self.id}>'


class PermissionMenuModel(BaseModel):
    """权限菜单多对多模型"""

    __tablename__ = 'permission_menu'
    __table_args__ = {
        'comment': '权限菜单多对多'
    }

    permission_id = db.Column(INTEGER(unsigned=True), comment='权限ID')
    menu_id = db.Column(INTEGER(unsigned=True), comment='菜单ID')

    def __repr__(self):
        return f'<RoleMenuModel {self.id}>'

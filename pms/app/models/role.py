from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER

from . import db
from .base import BaseModel


class RoleModel(BaseModel):
    """角色模型"""

    __tablename__ = "role"
    __table_args__ = {
        'comment': '角色表，角色可继承'
    }

    name = db.Column(String(20), nullable=False, unique=True, comment='角色名称')
    remark = db.Column(String(200), nullable=True, comment='备注')

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

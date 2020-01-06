from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER

from . import db
from .base import BaseModel


class MenuModel(BaseModel):
    """菜单模型"""

    __tablename__ = 'menu'
    __table_args__ = {
        'comment': '菜单表'
    }

    name = db.Column(String(20), nullable=False, unique=True, comment='名称')
    url = db.Column(String(100), nullable=False, comment='链接')
    order = db.Column(INTEGER(unsigned=True), default=0, comment='排序')

    def __repr__(self):
        return f'<MenuModel {self.id}>'

from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT

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
    common = db.Column(TINYINT(unsigned=True), default=1, comment='是否为公共菜单，1: 是  0: 否')

    @staticmethod
    def get_common_menu():
        """获取公共菜单"""
        menus = MenuModel.query.filter(MenuModel.common == 1).all()
        return [item.to_json() for item in menus]

    def __repr__(self):
        return f'<MenuModel {self.id}>'

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'url': self.url, 'order': self.order}

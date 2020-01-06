from sqlalchemy import String
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import db
from app.models.base import BaseModel


class UserModel(BaseModel):
    """用户模型"""

    __tablename__ = 'user'
    __table_args__ = {
        'comment': '用户表'
    }

    name = db.Column(String(20), nullable=False, unique=True, comment='登录名')
    _password = db.Column(String(128), name='password', nullable=False, comment='密码，hash散列')

    remark = db.Column(String(300), nullable=True, comment='备注，做一些小记录')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self._password, raw_password)

    def __repr__(self):
        return f'<UserModel {self.id}>'

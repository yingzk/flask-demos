from sqlalchemy import String
from werkzeug.security import generate_password_hash, check_password_hash

from app import MyException
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

    roles = db.relationship(
        'RoleModel',
        secondary='role_user',
        primaryjoin='UserModel.id == RoleUserModel.user_id',
        secondaryjoin='RoleUserModel.role_id == RoleModel.id',
        uselist=True,
        backref='users'
    )

    def get_permissions(self):
        return [{item.id: item.get_permissions()} for item in self.roles]

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self._password, raw_password)

    @staticmethod
    def login(form):
        """
        :param form: Login form
        :return:
        """
        name = form.get('name')
        password = form.get('password')
        if name and password:
            user = UserModel.query.filter(UserModel.name == name).first_or_404('User not exists')
            if user.check_password(password):
                return user.to_json()
            else:
                raise MyException('password incorrect')
        else:
            raise MyException('form error')

    @staticmethod
    def get_menu(uid, role):
        """get user menu"""
        # Step1 get user roles
        user = UserModel.query.get(uid)
        print(user.get_permissions())

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'remark': self.remark}

    def __repr__(self):
        return f'<UserModel {self.id}>'

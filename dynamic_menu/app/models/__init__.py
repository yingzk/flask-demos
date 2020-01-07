from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import UserModel
from .menu import MenuModel
from .permission import PermissionModel, PermissionRoleModel, PermissionMenuModel
from .role import RoleModel, RoleRoleModel, RoleUserModel

ModelList = {
    'user': UserModel,
    'menu': MenuModel,
    'permission': PermissionModel,
    'permission_role': PermissionRoleModel,
    'permission_menu': PermissionMenuModel,
    'role': RoleModel,
    'role_role': RoleRoleModel,
    'role_user': RoleUserModel
}

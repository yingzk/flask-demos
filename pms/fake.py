"""生成测试数据"""
from app import create_app

from app.models import db, UserModel, MenuModel, PermissionModel, RoleModel, PermissionMenuModel, PermissionRoleModel, \
    RoleUserModel, RoleRoleModel


def generate_user():
    for i in range(1, 11):
        user = UserModel(name=f'ying{i}', password='123', remark=f'ying{i}')
        db.session.add(user)
    db.session.commit()


def generate_menu():
    fake_menus = [
        ('首页', '/', 0),
        ('新增项目', '/add/project', 1),
        ('项目详情', '/project/detail', 2),
        ('修改项目', '/project/update', 3),
        ('删除项目', '/project/delete', 4),
        ('修改用户', '/user/update', 5),
        ('删除用户', '/user/delete', 6)
    ]

    for fake_menu in fake_menus:
        menu = MenuModel(name=fake_menu[0], url=fake_menu[1], order=fake_menu[2])
        db.session.add(menu)
    db.session.commit()


def generate_permission():
    fake_permissions = ['新增项目', '修改项目', '删除项目', '修改用户', '删除用户']
    # 没有权限，默认可以访问首页和项目详情
    for fake_permission in fake_permissions:
        permission = PermissionModel(name=fake_permission, remark=fake_permission)
        db.session.add(permission)
    db.session.commit()


def generate_role():
    fake_roles = ['普通用户', '项目管理员', '用户管理员', '超级管理员']
    for fake_role in fake_roles:
        role = RoleModel(name=fake_role, remark=fake_role)
        db.session.add(role)
    db.session.commit()


def generate_role_role():
    # 生成角色角色的继承
    # 超级管理员继承项目管理员和角色管理员
    fake_records = [
        (4, 2),
        (4, 3)
    ]
    for fake_record in fake_records:
        role_role = RoleRoleModel(role_id=fake_record[0], parent_id=fake_record[1])
        db.session.add(role_role)
    db.session.commit()


def generate_permission_menu():
    fake_records = [
        (1, 2),
        (2, 4),
        (3, 5),
        (4, 6),
        (5, 7),
    ]
    for fake_record in fake_records:
        permission_menu = PermissionMenuModel(permission_id=fake_record[0], menu_id=fake_record[1])
        db.session.add(permission_menu)
    db.session.commit()


def generate_permission_role():
    face_records = [
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 4),
        (3, 5),
    ]
    for face_record in face_records:
        permission_role = PermissionRoleModel(permission_id=face_record[1], role_id=face_record[0])
        db.session.add(permission_role)
    db.session.commit()


def generate_role_user():
    # 给第一个用户添加管理员权限
    role_user = RoleUserModel(role_id=4, user_id=1)
    db.session.add(role_user)
    db.session.commit()


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        generate_user()
        generate_menu()
        generate_permission()
        generate_role()
        generate_role_role()
        generate_permission_menu()
        generate_permission_role()
        generate_role_user()

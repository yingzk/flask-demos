from sqlalchemy.dialects.mysql import INTEGER

from app.models import db
from datetime import datetime
from sqlalchemy.sql.functions import now, current_timestamp


class BaseModel(db.Model):
    """模型基类"""

    __abstract__ = True

    # 这里的ID可加可不加，这个demo很小，所以统一用integer，如果是其他类型，请在表中具体写出
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment='主键ID')
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now, server_default=now(),
                            server_onupdate=current_timestamp(), onupdate=datetime.now, comment='更新时间')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now, server_default=now(), comment='创建时间')

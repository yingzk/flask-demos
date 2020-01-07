from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db
from app.models import ModelList

app = create_app()
Migrate(app, db)
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()

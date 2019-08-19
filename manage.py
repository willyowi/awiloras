from app import create_app,db
from flask_script import manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Session

app = create_app('development')

manager=Manager(app)
manager.add_command('server',Server)

manager=Manager(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict (app=app,db=db,User=User,)
if __name__=='__main__':
    manager.run()
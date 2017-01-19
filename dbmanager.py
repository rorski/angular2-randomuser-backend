from flask.ext.script import Manager, Shell, prompt_bool
from src import app

manager = Manager(app)

@manager.command
def dropdb():
    ''' Drop the database and delete the data '''
    if prompt_bool("Are you sure you want to lose all your data?"):
        db.drop_all()

@manager.command
def createdb():
    ''' Create the database '''
    create_app()

@manager.command
def rebuilddb():
    ''' Drop and rebuild the database '''
    if prompt_bool("Are you sure you want to lose all your data?"):
        dropdb()
        createdb()

@manager.command
def populate(users=False, events=False, pics=False):
    '''
        Populate the database with test data 
        (See seed_db.py)
    '''
    pass


if __name__ == "__main__":
    manager.run()

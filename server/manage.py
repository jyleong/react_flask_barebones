# manage.py

import os
import datetime
import time
from random import randint
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from server.app_file import db, create_app, config_name
from server import models

app = create_app(config_name)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    '''
    Assumes you have already have sleeportant database
    db init, and upgrade the databases
    method to create some initial users locally and insert to database
    make sleep records for each user for a large date range ~100-200 days
    :return:
    '''
    print("Seeding database with initial users")
    user1 = models.User(username="Rick", email="rickkyg@email.com")
    user2 = models.User(username="Talia", email="testTalia@fakeymail.com")
    user3 = models.User(username="Christina", email="christinaSteinsGate@email.com")
    


    db.session.add_all([user1, user2, user3])
    db.session.flush()
    db.session.commit()
    print("Users created!")
    
    return

if __name__ == '__main__':
    manager.run()
# models.py
# created by James L 07/07/2017

# file for all our database related python objects, used for ORM

from server.app_file import db
import datetime

# class User(db.Model):
#     """The test case table in mera_db"""
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60))
#     sleeprecord = db.relationship('SleepRecord', backref='sleeprecords', lazy='dynamic')


#     def __init__(self, name):
#         self.name = name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(
            self, username, email,
            created_at=datetime.datetime.utcnow()):
        self.username = username
        self.email = email
        self.created_at = created_at

# class SleepRecord(db.Model):
#     """The test case table in sleeportant"""
#     __tablename__ = "sleeprecords"

#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey('users.id'))
#     sleepState = db.Column(db.String(60)) # GOOD, OKAY, BAD
#     startTime = db.Column(db.BIGINT)
#     endTime = db.Column(db.BIGINT)
#     fullTimeSlept = db.Column(db.Integer)
#     date = db.Column(db.BIGINT)
#     timeToSleep = db.Column(db.Integer)
#     timeWokenUp = db.Column(db.Integer)
#     durationWokenUp = db.Column(db.Integer)


#     def __init__(self, userId, sleepState, startTime, endTime, fullTimeSlept,
#                  date, timeToSleep, timeWokenUp, durationWokenUp):
#         self.userId = userId
#         self.sleepState = sleepState
#         self.startTime = startTime
#         self.endTime = endTime
#         self.fullTimeSlept = fullTimeSlept
#         self.date = date
#         self.timeToSleep = timeToSleep
#         self.timeWokenUp = timeWokenUp
#         self.durationWokenUp = durationWokenUp
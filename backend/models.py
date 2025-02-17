from app import db
import datetime


class Habits(db.Model):
    __tablename__ = "habits"

    hid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"Habit with name {self.name}"

from app import db
import datetime


class Habit(db.Model):
    __tablename__ = "habits"

    habit_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"Habit with name {self.name}"

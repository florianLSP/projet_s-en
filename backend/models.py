from app import db
import datetime


class Habit(db.Model):
    __tablename__ = "habits"

    habit_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now)
    habit_logs = db.relationship(
        "HabitLog", back_populates="habit", cascade="all, delete-orphan"
    )
    emoji = db.Column(db.Text)

    def __repr__(self):
        return f"Habit with name {self.name}"


class HabitLog(db.Model):
    __tablename__ = "habit_logs"

    habit_log_id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.habit_id"), nullable=False)
    date = db.Column(db.DateTime)

    habit = db.relationship("Habit", back_populates="habit_logs")

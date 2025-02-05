from app import db


class Habits(db.Model):
    __tablename__ = "habits"

    hid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Habit with name {self.name}"

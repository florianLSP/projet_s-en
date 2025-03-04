from flask import request, jsonify
from models import Habit, HabitLog
from datetime import datetime
from sqlalchemy import desc


def register_routes(app, db):
    @app.route("/habits", methods=["GET", "POST"])
    def habits():
        if request.method == "GET":
            return get_habits()

        elif request.method == "POST":
            return post_habit()

    @app.route("/habit/<id>", methods=["DELETE"])
    def delete_habit(id):
        habit = Habit.query.get(id)
        if not habit:
            return jsonify({"error": "Habitude introuvable"}), 404

        db.session.delete(habit)
        db.session.commit()

        return jsonify({"message": "L'habitude a été supprimée"}), 200

    @app.route("/habit/<id>", methods=["GET"])
    def habit(id):
        if request.method == "GET":
            query = Habit.query.get(id)
            habit = {
                "id": query.habit_id,
                "name": query.name,
                "description": query.description,
                "creationDate": query.creation_date,
            }
            if not habit:
                return jsonify({"error": "Habitude introuvable"}), 404

            return jsonify(habit)

    def get_habits():
        habits = []
        for habit in Habit.query.all():
            habits.append(
                {
                    "id": habit.habit_id,
                    "name": habit.name,
                    "description": habit.description,
                    "creationDate": habit.creation_date,
                    "habitLogs": [
                        {"habit_id": log.habit_id, "date": log.date}
                        for log in HabitLog.query.filter_by(habit_id=habit.habit_id)
                        .order_by(desc(HabitLog.date))
                        .all()
                    ],
                    "emoji": habit.emoji,
                }
            )
        return jsonify(habits)

    def post_habit():
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "le champ 'name' est requis"}), 400

        new_habit = Habit(
            name=data["name"], description=data["description"], emoji=data["emoji"]
        )
        db.session.add(new_habit)
        db.session.commit()

        if len(data["habitLogs"]) > 0:
            for habit_log in data["habitLogs"]:
                date_str = habit_log["date"]
                date_str = date_str.replace("Z", "")
                log = HabitLog(
                    habit_id=new_habit.habit_id,
                    date=datetime.fromisoformat(date_str),
                )
                db.session.add(log)
                db.session.commit()

            return jsonify(
                {
                    "message": "Habitude ajoutée avec succès",
                    "habit": {
                        "id": new_habit.habit_id,
                        "name": new_habit.name,
                        "description": new_habit.description,
                        "creationDate": new_habit.creation_date,
                        "habit_logs": [
                            {"habit_id": log.habit_id, "date": log.date}
                            for log in new_habit.habit_logs
                        ],
                        "emoji": new_habit.emoji,
                    },
                }
            ), 201

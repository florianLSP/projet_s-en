from flask import request, jsonify
from models import Habits


def register_routes(app, db):
    @app.route("/habits", methods=["GET", "POST"])
    def habits():
        if request.method == "GET":
            habits = []
            for habit in Habits.query.all():
                habits.append(
                    {
                        "id": habit.hid,
                        "name": habit.name,
                        "creationDate": habit.creation_date,
                    }
                )
            return jsonify(habits)

        elif request.method == "POST":
            data = request.get_json()
            if not data or "name" not in data:
                return jsonify({"error": "le champ 'name' est requis"}), 400

            new_habit = Habits(name=data["name"])
            db.session.add(new_habit)
            db.session.commit()

            return (
                jsonify(
                    {
                        "message": "Habitude ajoutée avec succès",
                        "habit": {
                            "id": new_habit.hid,
                            "name": new_habit.name,
                            "creationDate": new_habit.creation_date,
                        },
                    }
                ),
                201,
            )

    @app.route("/habit/<id>", methods=["DELETE"])
    def delete_habit(id):
        habit = Habits.query.get(id)
        if not habit:
            return jsonify({"error": "Habitude introuvable"}), 404

        db.session.delete(habit)
        db.session.commit()

        return jsonify({"message": "L'habitude a été supprimée"}), 200

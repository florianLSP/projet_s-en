from flask import render_template, request, jsonify
from models import Habits
from app import db


def register_routes(app, db):
    @app.route("/habits", methods=["GET"])
    def get_habits():
        habits = []
        for habit in Habits.query.all():
            habits.append({"id": habit.hid, "name": habit.name})
        return jsonify(habits)
    

    @app.route("/add_habit", methods=["POST"])
    def add_habits():
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "le champ 'name' est requis"}), 400
        
        new_habit = Habits(name=data["name"])
        db.session.add(new_habit)
        db.session.commit()

        return jsonify({"message": "Habitude ajoutée avec succès", "habit": {"id": new_habit.hid, "name": new_habit.name}}), 201


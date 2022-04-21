from flask import Blueprint, Flask, redirect, render_template, request

from models.human import Human
from models.biting import Biting
from models.zombie import Zombie
from repositories import human_repository, zombie_repository, biting_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route('/bitings')
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings = bitings)

# NEW
@bitings_blueprint.route("/bitings/new")
def new_biting():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans = humans, zombies = zombies)

# CREATE
@bitings_blueprint.route("/bitings", methods = ['POST'])
def create_biting():
    human_id = request.form['human_id']
    human = human_repository.select(human_id)
    zombie_id = request.form['zombie_id']
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie)
    biting_repository.save(biting)

    return redirect('/bitings')

# EDIT
@bitings_blueprint.route("/bitings/<id>/edit")
def edit_biting(id):
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    biting = biting_repository.select(id)
    return render_template('/bitings/edit.html', humans = humans, zombies = zombies, biting = biting)

# UPDATE
@bitings_blueprint.route("/bitings/<id>", methods = ['POST'])
def update_biting(id):
    human_id = request.form['human_id']
    human = human_repository.select(human_id)
    zombie_id = request.form['zombie_id']
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie, id)

    biting_repository.update(biting)
    return redirect('/bitings')


# DELETE
@bitings_blueprint.route("/bitings/<id>/delete", methods = ['POST'])
def delete_biting(id):
    biting_repository.delete(id)
    return redirect("/bitings")

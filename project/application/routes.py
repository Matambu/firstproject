
from application import app, db
from application.models import ForceUsers, Masters
from flask import render_template, request, redirect, url_for
from application.forms import ForceUsersForm, MastersForm


@app.route('/')
def index():
    all_forceusers = ForceUsers.query.all()
    all_masters = Masters.query.all()
    return render_template('index.html', all_forceusers = all_forceusers, all_masters = all_masters)


@app.route('/forceusers', methods=['GET', 'POST'])
def forceuser():
    form = ForceUsersForm()

    if request.method == "POST":
        forceuser = ForceUsers(
            name = form.name.data,
            power = form.power.data,
    
            
        )
        db.session.add(forceuser)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('forceusers.html', form = form)


@app.route('/add_master', methods=['GET', 'POST'])
def add_master():
    form = MastersForm()

    if request.method =="POST":
        Master = Masters(name = form.name.data, side = form.side.data)
       
        db.session.add(Master)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template('masters.html', form=form)


@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form = ForceUsersForm()
    ForceUser = ForceUsers.query.filter_by(id=id).first()
    if request.method == "POST":
        ForceUsers.name = form.name.data
        ForceUsers.power = form.power.data
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("forceusers.html", form = form,  ForceUsers = ForceUsers)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    Master =Masters.query.filter_by(id=id).first()
    db.session.delete(Master)
    db.session.commit()
    return redirect(url_for("index")) 


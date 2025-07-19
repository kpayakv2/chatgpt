from flask import Flask, render_template, request, redirect, url_for
from models import db, MaintenanceLog
from forms import MaintenanceLogForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    logs = MaintenanceLog.query.order_by(MaintenanceLog.date.desc()).all()
    return render_template('index.html', logs=logs)

@app.route('/add', methods=['GET', 'POST'])
def add_log():
    form = MaintenanceLogForm()
    if form.validate_on_submit():
        log = MaintenanceLog(
            part=form.part.data,
            mileage=form.mileage.data,
            notes=form.notes.data,
        )
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/edit/<int:log_id>', methods=['GET', 'POST'])
def edit_log(log_id):
    log = MaintenanceLog.query.get_or_404(log_id)
    form = MaintenanceLogForm(obj=log)
    if form.validate_on_submit():
        log.part = form.part.data
        log.mileage = form.mileage.data
        log.notes = form.notes.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, log=log)

@app.route('/delete/<int:log_id>', methods=['POST'])
def delete_log(log_id):
    log = MaintenanceLog.query.get_or_404(log_id)
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

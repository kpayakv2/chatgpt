from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MaintenanceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    part = db.Column(db.String(100), nullable=False)
    mileage = db.Column(db.Integer)
    notes = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    logs = MaintenanceLog.query.order_by(MaintenanceLog.date.desc()).all()
    return render_template('index.html', logs=logs)

@app.route('/add', methods=['GET', 'POST'])
def add_log():
    if request.method == 'POST':
        part = request.form['part']
        mileage = request.form.get('mileage') or None
        notes = request.form.get('notes')
        log = MaintenanceLog(part=part, mileage=mileage, notes=notes)
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
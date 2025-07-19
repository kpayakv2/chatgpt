from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Optional, NumberRange

class MaintenanceLogForm(FlaskForm):
    part = StringField('ชิ้นส่วน', validators=[DataRequired()])
    mileage = IntegerField('ระยะทาง', validators=[Optional(), NumberRange(min=0)])
    notes = TextAreaField('หมายเหตุ', validators=[Optional()])

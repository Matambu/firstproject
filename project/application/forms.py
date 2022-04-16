from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length



class ForceUsersForm(FlaskForm):
    name = StringField('Name')
    power = StringField('Power')
    submit = SubmitField("submit")

    

class MastersForm(FlaskForm):
    name =  StringField('Name')
    side = StringField("Side")
    submit = SubmitField('Add Master')

    
from wtforms import Form, TextField, validators
from wtforms.fields import SelectField
class Options(Form):
    #formula = SelectField('Formulas', 
    #                choices=[('epley','Epley'),('brzycki','Brzycki'),
    #                         ('lombardi', 'Lombardi'),('mayhew', 'Mayhew'),
    #                         ('oconner', "O'conner",), ('wathan', 'Wathan'),
    #                         ('lander', 'Lander')])
    weight = TextField('weight',[validators.Required()])
    reps = TextField('reps',[validators.Required()])

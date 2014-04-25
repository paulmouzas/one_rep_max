from wtforms import Form, BooleanField, TextField, PasswordField, validators, IntegerField

class Options(Form):
    #formula = SelectField('Formulas', 
    #                choices=[('epley','Epley'),('brzycki','Brzycki'),
    #                         ('lombardi', 'Lombardi'),('mayhew', 'Mayhew'),
    #                         ('oconner', "O'conner",), ('wathan', 'Wathan'),
    #                         ('lander', 'Lander')])
    weight = IntegerField('weight', [validators.Required(), validators.NumberRange(min=20, max=500)])
    reps = IntegerField('reps', [validators.Required(), validators.NumberRange(min=2, max=20)])

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Email, Regexp, StopValidation


class FeedbackForm(Form):

    feedback = StringField('Feedback', [Required()])

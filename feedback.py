from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Email, Regexp, StopValidation


class FeedbackForm(FlaskForm):

    feedback = StringField('Feedback', [Required()])

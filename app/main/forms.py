from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import Required


class PostForm(FlaskForm):
    
    title = StringField('title',validators=[Required()])
    blog = TextAreaField('blog ', validators=[Required()])
    category = SelectField('Type',choices=[('interview','interview blog'),('professional','professional blog'),('motivational','motivational blog')],validators=[Required()])  
    submit = SubmitField('Submit','success')
    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit','info')
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import Required,InputRequired


class PostForm(FlaskForm):
    
    title = StringField('title',validators=[Required()])
    blog = TextAreaField('post ', validators=[Required()])
    category = SelectField('Type',choices=[('interview','interview post'),('professional','professional post'),('motivational','motivational post')],validators=[Required()])  
    submit = SubmitField('Submit','success')
    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit','info')

class AddCommentForm(FlaskForm):
    body = StringField("Body", validators=[InputRequired()])
    submit = SubmitField("Post")    
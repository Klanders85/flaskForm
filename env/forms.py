# import wtf forms from flask and get the Form Class
from flask.ext.wtf import Form

# import the Classes from the wtf forms
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

# create a Class named ContactForm which will inherit the Form Class
class ContactForm(Form):
	# properties of the Class
	name  = TextField("Name", [validators.Required()])
	email = TextField("Email", [validators.Required(), validators.Email()])
	subject = TextField("Subject", [validators.Required()])
	message = TextAreaField("Message", [validators.Required()])
	submit = SubmitField("Send")
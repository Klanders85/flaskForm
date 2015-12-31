# import Flask and some of its methods
from flask import Flask, render_template, request, flash

# import Class created in forms.py named ContactForm
from forms import ContactForm

# not exactly sure what the .ext. is but I know it's what gets the mail Class from flask and Message and Mail are its methods
from flask.ext.mail import Message, Mail

# new instance of mail Class
mail = Mail()

# new instance of flask, saved as aoo
app = Flask(__name__)

# terminal logger and updates page upon save
app.debug = True

# secret key for something, not sure what. Never gets reference anywhere else...
app.secret_key = 'secretTestKey'

# email settings for sending mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
# email address and dev creds that the email is being sent from, if you have a no-reply@notifications.com domain, you would use that here.
app.config["MAIL_USERNAME"] = "kellylanders2@gmail.com"
app.config["MAIL_PASSWORD"] = "ipcdvlugcwpgqqvc"

# attaches mail instance to the flask app instance
mail.init_app(app)

# Home / Index Route
@app.route('/')
def index_view():
	print (request.headers)
	return render_template(
		"index.html",
		page_title = "Home"
	)

# About Route
@app.route('/about')
def about_view():
	print (request.headers)
	return render_template(
			"about.html",
			page_title = "About"
		)

# Services Route
@app.route('/services')
def services_view():
	print (request.headers)
	return render_template(
			"services.html",
			page_title = "Services"
		)

# Contact Route
@app.route('/contact' ,methods =['GET', 'POST'])
def contact_view():
	print (request.headers)

	# new instance of contactForm() Class
	form = ContactForm()

	# check to see if request coming in is a POST, if it is, see next check
	if request.method == 'POST':

		# check to see if form validates, show flash message if validate is false and render the contact view
		if form.validate() == False:
			flash('All fields are required!')
			return render_template(
				"contact.html",
				page_title = "Contact",
				form = form
			)
		# if form validate is true
		else:
			# message parameters
			msg = Message(form.subject.data, sender='kellylanders2@gmail.com', recipients=['klanders@trivie.com'])
	      	msg.body = """
	      	From: %s <%s>
	      	%s
	      	""" % (form.name.data, form.email.data, form.message.data)
	      	# send the message 
	      	mail.send(msg)

	      	return 'Form posted.'

	# if request method is a GET, then render the contact view
	elif request.method == "GET":
		return render_template(
			"contact.html",
			page_title = "Contact",
			form = form
		)


if __name__ == '__main__':
	app.run()
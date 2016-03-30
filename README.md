## Beyond Remodels

* * *

A website I built, using `HTML` `CSS` `Python` `Flask`

It is a site to show my client&s business (home renovation) with a goal to reach more people ie. more $$$

The front-end, nothing too crazy here, worth noting that a Mobile-First approach was use as well as Responsive Web Design techniquies are being used to respond to different mobile devices

There is a Contact view that has a simple contact form, that upon completion, will send that information from the form to an email address that can be designated, this back-end is written in Python, also utilizing the micro-framework Flask to handle the routing aspects to serve the templates.

WTForms being used to handle aspects of the form processcing and the emailing of the completed form.

Ok, now that we have that out of the way, let's get this environment installed!

* * *

### Clone the repo

Nothing wacky here, get the repo however you normally would

### Install Pip for Python

Run this in terminal `sudo easy_install pip`

**[Reference for pip installation](http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x)**

### Install Flask for Python

Run this in terminal `sudo pip install flask`

**[Reference for Flask installation](http://www1.cmc.edu/pages/faculty/alee/cs40/penv/installFlaskOnMac.html)**

_If you get hung up with the backend-install, do what I do...Google!_

### Install a Virtual Environment for Python...(optional)

Need to update this...gets a little tricky

### Up and Running

If everything went swimmingly, you should be able to cd into the `env` directory and run `. bin/activate`, you will see (env) somewhere in your file path (depending on your shell set-up) this is simply to let you know that you have activated your virtual environment, to deactivate the virtual environment, simply run `$deactivate` the (env) should disappear

Ok. So, if you haven&t yet, `cd` to your `env` directory and you should see an `app.py` file, that file contains all the routing code, as well as app initialization code. You will see that it is pretty well documented and most of the code in this repo has been documented also.

### Fire Up the Server

Now for the exciting part, back in terminal, and you are at your `env` directory, simply run, `python app.py`. If everything is working you should something along the lines of this...

`* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)` `* Restarting with stat` `* Debugger is active!` `* Debugger pin code: 135-663-957`

If that is what you are seeing, simply point your browser to [http://127.0.0.1:5000](http:localhost:5000)

Boom! You should be at the homepage! From there, code away! I will keep this repo up-to-date, and PRs are welcome! (especially design recommendations lol!)
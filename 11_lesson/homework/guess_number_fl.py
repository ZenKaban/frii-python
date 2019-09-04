from flask import Flask, request
import os
import random
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)

try:
    random.seed(os.environ['FLASK_RANDOM_SEED'])
except KeyError:
    print("Set ENV variable FLASK_RANDOM_SEED")

app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

count_success = 0
count_tries = 0
guessed = None

class ContactForm(FlaskForm):
    number = StringField(label='Name', validators=[
        validators.Length(min=1, max=25)
    ])

def get_random_number():
    guessed = random.randrange(1, 10)
    return guessed

@app.route('/', methods = ['GET'])
@app.route('/guess/', methods = ['POST'])
def home():
    global count_success
    global count_tries
    global guessed
    
    if request.method == "GET":
        guessed = get_random_number()
        print(guessed)
        return "Number generated"
    if request.method == "POST":
        count_tries += 1
        print(count_tries)
        number = ContactForm(request.form)
        number_int = int(number.data['number'])
        if number_int > guessed:
            result = ">, try again, number or tries " + str(count_tries)
        elif number_int < guessed:
            result = "<, try again, number or tries " + str(count_tries)
        elif number_int == guessed:
            count_success += 1
            print(count_success)
            result = "=, success, new number generated, number of successes " + str(count_success)
            guessed = get_random_number()
            print(guessed)
            
        return result

app.run()
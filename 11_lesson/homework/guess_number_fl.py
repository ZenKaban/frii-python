from flask import Flask, request
import os
import random
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)

random.seed(os.environ['FLASK_RANDOM_SEED'])
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)



class ContactForm(FlaskForm):
    number = StringField(label='Name', validators=[
        validators.Length(min=1, max=25)
    ])

def get_random_number():
    guessed = random.randrange(1, 10)
    with open("number.txt", 'w') as f:
        f.write(str(guessed))
    return guessed

@app.route('/', methods = ['GET'])
@app.route('/guess/', methods = ['POST'])
def home():
    
    if request.method == "GET":
        guessed = get_random_number()
        print(guessed)
        return "Number generated"
    if request.method == "POST":
        number = ContactForm(request.form)
        number_int = int(number.data['number'])
        with open("number.txt","r") as f:
            guessed = f.readline()
            guessed_int = int(guessed)
        if number_int > guessed_int:
            result = ">"
        elif number_int < guessed_int:
            result = "<"
        elif number_int == guessed_int:
            result = "=, new number generated"
            guessed = get_random_number()
            print(guessed)
            
        return result

app.run()
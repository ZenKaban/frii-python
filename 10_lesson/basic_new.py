from flask import Flask
app = Flask(__name__)

@app.route('/post/<int:number>')
def another_home1(number):
    return 'test view {}'.format(number)

@app.route('/post/<int:username>')
def another_home2(username):
    return 'hello user {}'.format(username)

@app.route('/post/<int:num1>/<int:num2>')
def get_sum(num1, num2):
    sum_n = int(num1) + int(num2)
    return str(sum_n)

@app.route('/post/<str1>/<str2>/<str3>')
def measure_string(str1, str2, str3):
    len(str1)
    
    return str(str_d)

app.run()
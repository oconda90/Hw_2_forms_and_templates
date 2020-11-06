from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    context = {
    'users_froyo_flavor' : request.args.get('flavor'),
    'users_froyo_toppings' : request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite Color? <br/>
        <input type="text" name="color"><br/>
        What is your animal!<br/>
        <input type="text" name="animal"><br/>
        What is your favorite City?<br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')

    return f"I didn't know {users_fav_color} {users_fav_animal} lived in {users_fav_city}!" 

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
    Enter a message to encrypt.</br>
    <input type="text" name="message"></br>
    <input type="submit" value="Submit!"></br>
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    user_phrase = request.form['message']
    scramble_phrase = sort_letters(user_phrase)
    return f'Here is your Message! {scramble_phrase}'
    


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    number1 = int(request.args.get('operand1'))
    number2 = int(request.args.get('operand2'))
    operand = request.args.get('operation')
    answer = 0

    if operand == "add" :
        answer = number1 + number2
    elif operand == "subtract" :
        answer = number1 - number2
    elif operand == "multiply" :
        answer = number1 * number2
    elif operand == "divide" :
        answer = number1 / number2
    
    context = {
        'number1' : number1,
        'number2' : number2,
        'operand' : operand,
        'answer' : answer
    }

    return render_template('calculator_results.html', **context)
  

# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()

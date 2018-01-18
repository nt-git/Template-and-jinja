"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
# decorator
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Show madlib form"""

    answer = request.args.get("show_madlib")
    if answer == "no":
        return render_template("goodbye.html")

    #return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective)
    return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    "Show madlib results"
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    adjective2 = request.args.getlist("adjective2")
    place = request.args.getlist("place")
    # adjective2 = adjective2[3:-2]
    # return with a list
    print adjective2

    return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective, adjective2=adjective2, place=place)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)

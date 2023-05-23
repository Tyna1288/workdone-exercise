"""Madlibs Stories."""
from stories import story
from flask import render_template, request, Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/Madlibs")
def ask_questions():
    """Generate and show form to ask words."""
    prompts = story.prompts
    return render_template("ask.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)


# Here's a story to get you started



from cgitb import text
from distutils.log import debug
from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from random import choice, sample
from stories import story1, story2, story3, stories 

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'secrettttkeyyy'
# debug = DebugToolbarExtension(app)


@app.route("/")
def selectstory():
    return render_template("selectstory.html", stories = stories.values())

@app.route("/writestory")
def write_story():
 
    option = request.args["storyoption"] #this gives us the value of the "storyoption" key which is either 1,2 or 3 depending on the story the user selects. so the variable "option" will either be numbers 1,2 or 3
    story = stories[option] #this will give us the story instance with the key of either 1,2,3 (as defined in stories )
    prompts = story.prompts #we will take that story instance and get the prompts -  the prompt will be that story.prompts which is the words they passed in
    # print("option", option, "story", story)
    return render_template("home.html", prompts = prompts, option=option) #in the home.html we are creating a hidden <input type="hidden" name = "storyoption" value="{{option}}"> so we have a way to grab the "storyoption" again to pass into the /story route to make the story in request.arg

@app.route("/story")
def make_story():

    option = request.args["storyoption"] #this again gives us the value of the "storyoption" key which is either 1,2 or 3 depending what the <input> has stored 
    # print("optionn", option)
    story = stories[option] #this will give us the story with the key of either 1,2,3 (as defined in stories )
    text = story.generate(request.args) #then we will use the generate() method on that story to generate the text
    # story1= stories["1"]
    # story2= stories["2"]
    # story3= stories["3"]
    # print("story", request.args)
    # text1 = story1.generate(request.args)
    # text2 = story2.generate(request.args)
    # text3 = story3.generate(request.args)
    
    return render_template("story.html", text=text)
    text1 =text1, text2= text2, text3=text3


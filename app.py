from flask import Flask,render_template,request
import google.generativeai as palm

api = "AIzaSyCaQcgKn95ZO6AR1t2PXzk9UydTkt4sWZQ"
palm.configure(api_key=api)
model = {"model": "models/text-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_FAQ",methods=["GET","POST"])
def financial_FAQ():
    return(render_template("financial_FAQ.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.generate_text(prompt=q, **model)
    return(render_template("makersuite.html",r=r.result))

@app.route("/joke", methods=["GET","POST"])
def joke():
    joke_text = "Which noodle is the heaviest? Wanton (one-tonne) noodles."
    return render_template("joke.html", joke=joke_text)

if __name__ == "__main__":
    app.run()

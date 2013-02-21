from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/php")
def php():
    return render_template("php/php.html")

@app.route("/php/facebook")
def facebook_php():
    return render_template("php/facebook.html")

@app.route("/php/no_facebook")
def no_facebook_php():
    return render_template("php/no_facebook.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/rails")
def rails():
    return render_template("rails/rails.html")

@app.route("/rails/online")
def online_rails():
    return render_template("rails/online.html")

@app.route("/rails/offline")
def offline_rails():
    return render_template("rails/offline.html")

@app.route("/compiled")
def compiled():
    return render_template("compiled.html")

@app.route("/hipster")
def hipster():
    return render_template("hipster.html")

@app.route("/js")
def js():
    return render_template("js.html")

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
from flask.ext.cache import Cache
app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@cache.cached(timeout=50)
@app.route("/")
def index():
    return render_template("index.html")

@cache.cached(timeout=50)
@app.route("/php")
def php():
    return render_template("php/php.html")

@cache.cached(timeout=50)
@app.route("/php/facebook")
def facebook_php():
    return render_template("php/facebook.html")

@cache.cached(timeout=50)
@app.route("/php/no_facebook")
def no_facebook_php():
    return render_template("php/no_facebook.html")

@cache.cached(timeout=50)
@app.route("/python")
def python():
    return render_template("python.html")

@cache.cached(timeout=50)
@app.route("/rails")
def rails():
    return render_template("rails/rails.html")

@cache.cached(timeout=50)
@app.route("/rails/online")
def online_rails():
    return render_template("rails/online.html")

@cache.cached(timeout=50)
@app.route("/rails/offline")
def offline_rails():
    return render_template("rails/offline.html")

@cache.cached(timeout=50)
@app.route("/compiled")
def compiled():
    return render_template("compiled.html")

@cache.cached(timeout=50)
@app.route("/hipster")
def hipster():
    return render_template("hipster.html")

@cache.cached(timeout=50)
@app.route("/js")
def js():
    return render_template("js.html")

if __name__ == "__main__":
    app.run()

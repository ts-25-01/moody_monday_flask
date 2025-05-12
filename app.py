from flask import Flask

#an dieser stelle wollen wir das flask objekt initialisieren
app = Flask(__name__)

# hier fangen wir damit an die routen zu definieren
@app.route("/")
def homepage():
    return "Heute ist der Moody Monday"

@app.route("/about")
def about():
    return "This is about the Moody Monday Coffe Need!"

if __name__ == "__main__":
    app.run(debug=True)

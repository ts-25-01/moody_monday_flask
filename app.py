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

# Info-Seite, wo Informationen ausgegeben werden 
## Schritt 1: Dekorator für route-Funktion vom app-Objekt definieren
## Wichtig: In Klammern danach angeben den Pfad für diese Route
@app.route("/info")
## Schritt 2: Funktionsdefinition der Funktion, die ausgeführt werden soll in der Route
def info():
    ## Schritt 3: Definiere was beim Aufruf der Route ausgeführt werden soll
    return "Das sind die wichtigen Informationen über unseren Moody Monday!"

# Parameter = Platzhalter für variablen Input
# Wenn jemand kommt, begrüße ihn!
# einfacher String-Parameter
@app.route("/greet/<name>")
def greet(name):
    return f"Hallo, {name}"

@app.route("/greet")
def main_greet():
    return "Das ist die Willkommensseite"

# Integer-Parameter, wo wir Typkonvertierung durchführen wollen
# Berechnung des Quadrats
@app.route("/square/<int:number>")
def square_function(number):
    result = number * number
    return f"Das Quadrat von {number} ist {result}"

# Pfad-Parameter (d.h. kann auch Schrägstriche enthalten)
@app.route("/files/<path:file_path>")
def show_file(file_path):
    return f"Datei: {file_path}"


# hier starten wir die main funktion
if __name__ == "__main__":
    app.run(debug=True)

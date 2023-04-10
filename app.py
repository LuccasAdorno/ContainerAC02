from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Luccas Adorno Albuquerque - RA: 2201890"

if __name__ == "__main__":
    app.run(debug=True)
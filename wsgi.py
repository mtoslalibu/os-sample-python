from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    print("Merdali!")
    return "Hello World!"

if __name__ == "__main__":
    print("Here")
    application.run(port=8080)

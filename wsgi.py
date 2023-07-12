from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    print("Merdali 8080!")
    return "Hello World!"

if __name__ == "__main__":
    print("Merdo 8080")
    application.run(port=8080)

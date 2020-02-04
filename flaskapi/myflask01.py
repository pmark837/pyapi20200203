#!/usr/bin/python3


from flask import Flask #from the library flask, look for the class Flask

app = Flask(__name__)

# @ is a decorator, describes when a code should run.
@app.route("/")

def hello_world(): #function, normall ran only when called.
    return "Hello Zachs Class!!!!"

@app.route("/hello/<name>")
def hello_user(name):
    return f"Hi there {name}"

if __name__ == "__main__":
    app.run(port=5006)

from flask import Flask
from rocket import *

app = Flask(__name__)

@app.route("/up/<int:seconds>")
def up(seconds):
    rocket = CircusRocket()
    rocketManager = RocketManager(rocket)
    rocketManager.up().sleep(seconds).stop()
    return "up"

@app.route("/down/<int:seconds>")
def down(seconds):
    rocket = CircusRocket()
    rocketManager = RocketManager(rocket)
    rocketManager.down().sleep(seconds).stop()
    return "down"

@app.route("/left/<int:seconds>")
def left(seconds):
    rocket = CircusRocket()
    rocketManager = RocketManager(rocket)
    rocketManager.left().sleep(seconds).stop()
    return "left"


@app.route("/right/<int:seconds>")
def right(seconds):
    rocket = CircusRocket()
    rocketManager = RocketManager(rocket)
    rocketManager.right().sleep(1).stop()
    return "right"


if __name__ == "__main__":
    app.run()

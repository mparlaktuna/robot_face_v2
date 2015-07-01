from flask import Flask, jsonify, render_template, request, session, g, redirect, url_for, abort,  flash
from robot import Robot

app = Flask(__name__)

robot = Robot('bilgin')
robot.setup_robot()


@app.route('/')
def show_homepage():
    return render_template('anasayfa.html')


@app.route('/motor/', methods=["GET","POST"])
def show_motor():
    value = request.args.get('')
    return render_template('motorlar.html', entries=robot.motor_list.values())


if __name__ == '__main__':
    app.run()

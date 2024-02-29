from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rps_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class GameRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String(50))
    computer_choice = db.Column(db.String(50))
    result = db.Column(db.String(50))

# 나머지 Flask 애플리케이션 코드...

@app.route('/example')
def example():
    return 'This is an example route.'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



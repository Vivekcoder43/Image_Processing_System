
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import init_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

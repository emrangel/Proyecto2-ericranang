from flask import Flask, render_template
from controllers.controller import *
from dotenv import load_dotenv
from db import db
import os

load_dotenv(override=True)

app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")
app.register_blueprint(heladeria_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
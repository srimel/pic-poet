import flask
from flask.views import MethodView

app = flask.Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
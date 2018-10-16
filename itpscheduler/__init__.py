from flask import Flask

app = Flask(__name__)

from . import api
app.register_blueprint(api.bp)

from . import routes
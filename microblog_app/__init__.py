from flask import Flask

app = Flask(__name__)

from microblog_app import routes

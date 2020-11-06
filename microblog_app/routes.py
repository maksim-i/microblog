from microblog_app import app

@app.route('/')
@app.route('/index')
def index():
    return "microblog"

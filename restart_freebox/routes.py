from .app import app
from .restart_freebox import restart_freebox


@app.route('/')
def hello_world():
    return "OK", 200


@app.route('/restartfreebox/<password>/')
def restart(password):
    restart_freebox(password)
    return "Freebox restarted", 200

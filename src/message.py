from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

somelist = ['apple', 'peas', 'juice', 'orange']
i=0

@app.route('/')

def index():
    return render_template('message.html')

i = 0

@socketio.on('message')
def handle_msg(msg):
    global i
    if i < len(somelist):
        socketio.send(somelist[i])
        i += 1


if __name__ == '__main__':
    socketio.run(app)
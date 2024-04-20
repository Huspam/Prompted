import socketio

SERVER_ADDRESS = 'http://13.57.33.95:3001'
# SERVER_ADDRESS = 'http://localhost:3001'

# Create your SocketIO client instance
sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connected to server')


@sio.event
async def disconnect():
    print('disconnected from server')


async def connect_to_game(username):
    await sio.connect(SERVER_ADDRESS)
    await sio.emit("joinGame", username)


@sio.event
def join_accepted(numUsers):
    print(numUsers)
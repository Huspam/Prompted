import socketio

SERVER_ADDRESS = 'http://50.18.13.223:3001'

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


# def join_accepted():
#     num_players = sio.call("get_num_players")
#     return num_players
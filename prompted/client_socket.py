import socketio
import os

NUM_PLAYERS = 0
PROMPT_IMG = None

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
def join_accepted(num):
    global NUM_PLAYERS
    NUM_PLAYERS = num


async def game_start():
    files = os.listdir('./assets')
    await sio.emit("gameStart", files)

async def submit_prompt(prompt):
    await sio.emit("submitPrompt", prompt)    



@sio.event
def game_started(img):
    print(img)
    global PROMPT_IMG
    PROMPT_IMG = img
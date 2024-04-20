import reflex as rx
import asyncio
import socketio
from prompted.join import index
from prompted.game import game

SERVER_ADDRESS = 'http://50.18.13.223:3001'

# Create your SocketIO client instance
sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connected to server')


@sio.event
async def disconnect():
    print('disconnected from server')

async def start_server():
    await sio.connect(SERVER_ADDRESS)
    await sio.wait()

asyncio.run(start_server())


# Add state and page to the app with Socket.IO client
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="medium", accent_color="mint"
    ),
    socket_app=sio
)

app.add_page(index, title="Reflex:Join")
app.add_page(game, title="Reflex:Game")
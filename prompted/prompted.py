import reflex as rx
from prompted.join import index
from prompted.game import game

# Add state and page to the app with Socket.IO client
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="medium", accent_color="mint"
    ),
)

app.add_page(index, title="Reflex:Join")
app.add_page(game, title="Reflex:Game")
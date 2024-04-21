import reflex as rx
from prompted.state import State

def lobby () -> rx.Component:
    """The Lobby Page"""

    return rx.center(
        rx.vstack(
            rx.heading("Welcome to the Lobby👋", font_size="1.5em"),
            rx.text("Player Count: ", State.numPlayers),
            rx.divider(),
            rx.button(
                "Start Game",
                id="start_button",
                on_click=State.start_game,
                color_scheme="grass"
            ),
            rx.divider(),
            rx.vstack(
                rx.foreach(
                    State.usernames,
                    lambda username: rx.text(username)
                ),
                align="center"
            ),
            height="30em",
            width="25em",
            bg="white",
            padding="2em",
            align="center",
            border_radius="2em",
            spacing="6"
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )

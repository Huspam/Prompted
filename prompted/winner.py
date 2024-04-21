import reflex as rx
from prompted.state import State

def winner():
    return rx.center(
        rx.vstack(
            rx.heading("Winner!👋", font_size="1.5em"),
            rx.text(State.winner[0]),
            rx.image(State.winner[1]),
            rx.text("Points: ", State.winner[2]),
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

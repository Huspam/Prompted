import reflex as rx
from prompted.state import State

def index () -> rx.Component:
    """The Join Page"""
    return rx.center(
        rx.vstack(
            rx.heading("Prompted.io", font_size="2em"),
            rx.form(
                rx.vstack(
                    rx.input(
                        id="username",
                        placeholder="Enter your name...",
                        size="3",
                    ),
                    rx.divider(),
                    rx.button(
                        "Join A Game",
                        type="submit",
                        size="3",
                    ),
                    align="stretch",
                    spacing="4",
                ),
                width="100%",
                on_submit=State.join_game,
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

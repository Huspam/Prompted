import reflex as rx
from prompted.state import State

def index () -> rx.Component:
    """The Join Page"""
    return rx.center(
        rx.vstack(
            rx.heading("Prompted.io", font_size="1.5em"),
            rx.form(
                rx.vstack(
                    rx.input(
                        id="user_name",
                        placeholder="Enter your name",
                        size="3",
                    ),
                    rx.button(
                        "Join A Game",
                        type="submit",
                        size="3",
                    ),
                    align="stretch",
                    spacing="2",
                ),
                width="100%",
                on_submit=State.join_game,
            ),
            rx.divider(),
            rx.cond(
                State.join_processing,
                rx.chakra.circular_progress(is_indeterminate=True),
                rx.redirect(
                    "/game"
                )
            ),
            width="25em",
            bg="white",
            padding="2em",
            align="center",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )

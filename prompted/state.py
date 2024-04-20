import reflex as rx

from prompted.client_socket import connect_to_game

class State(rx.State):
    """The app state."""

    numberOfPlayers = 0

    @rx.background
    async def join_game(self, form_data: dict[str, str]):
        """Join a game session"""
        username: str = form_data["username"]
        try:
            await connect_to_game(username)
            # self.numberOfPlayers = join_accepted()
            yield rx.redirect("/game")
        except Exception as ex:
            yield rx.window_alert(f"Error with joining a game. {ex}")
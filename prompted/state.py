import reflex as rx
import time

import prompted.client_socket as socket

class State(rx.State):
    """The app state."""

    numPlayers = socket.NUM_PLAYERS
    promptImg = ""

    @rx.var
    def promptImage(self):
        return self.promptImg

    @rx.background
    async def join_game(self, form_data: dict[str, str]):
        """Join a game session"""
        username: str = form_data["username"]
        try:
            await socket.connect_to_game(username)
            yield rx.redirect("/lobby")
            yield State.update_players()  
            yield State.check_game_started()
        except Exception as ex:
            yield rx.window_alert(f"Error with joining a game. {ex}")


    @rx.background
    async def update_players(self):
        while True:
            async with self:
                self.numPlayers = socket.NUM_PLAYERS
            time.sleep(1)


    @rx.background
    async def start_game(self):
        await socket.game_start()


    @rx.background
    async def check_game_started(self):
        while True:
            async with self:
                if socket.PROMPT_IMG:
                    self.promptImg = socket.PROMPT_IMG
                    yield rx.redirect("/game")
                    break
            # time.sleep(1)

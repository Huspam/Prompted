import reflex as rx
import openai
import os
from dotenv import load_dotenv
import base64

import prompted.client_socket as socket

_client = None
load_dotenv()

def get_openai_client():
    global _client
    if _client is None:
        _client = openai.OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

    return _client

class State(rx.State):
    """The app state."""
    image_url = ""
    image_processing = False
    image_made = False

    async def get_dalle_result(self, form_data: dict[str, str]):
        prompt_text: str = form_data["prompt_text"]
        self.image_made = False
        self.image_processing = True
        # Yield here so the image_processing take effects and the circular progress is shown.
        yield
        try:
            response = get_openai_client().images.generate(
                prompt=prompt_text, n=1, size="1024x1024"
            )
            self.image_url = response.data[0].url
            await socket.image_send(self.image_url)
            self.image_processing = False
            self.image_made = True
            yield
        except Exception as ex:
            self.image_processing = False
            yield rx.window_alert(f"Error with OpenAI Execution. {ex}")
    
    numPlayers = socket.NUM_PLAYERS
    usernames = []
    promptImg = ""
    gallery = []

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
                self.usernames = socket.USERNAMES


    @rx.background
    async def start_game(self):
        await socket.game_start()


    @rx.background
    async def check_game_started(self):
        while True:
            async with self:
                if socket.PROMPT_IMG:
                    self.promptImg = "/" + os.listdir("assets")[socket.PROMPT_IMG]
                    print(self.promptImg)
                    yield rx.redirect("/game")
                    yield State.check_gallery()
                    break


    # @rx.background
    # async def submit_prompt(self, prompt):
        
    #     yield State.check_image_url()
    #     yield State.check_gallery()


    # @rx.background
    # async def check_image_url(self):
    #     while True:
    #         async with self:
    #             if socket.IMG_URL:
    #                 self.image_url = socket.IMG_URL
    #                 break


    @rx.background
    async def check_gallery(self):
        while True:
            async with self:
                if socket.GALLERY:
                    self.gallery = socket.GALLERY.copy()
                    yield rx.redirect('/voting')
                    break
    
    # @rx.background
    # async def get_prompt_img(self):
    #     async with self:
    #         print(self.promptImg)
    #         return self.promptImg
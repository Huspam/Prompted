import reflex as rx
from dotenv import load_dotenv
import os
import openai
import random

# _client = None
# load_dotenv()

# def get_openai_client():
#     global _client
#     if _client is None:
#         _client = openai.OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

#     return _client

def fetch_random_img():
    random_image_filename = random.choice(os.listdir("assets"))
    return random_image_filename

def game(): 
    return rx.center(
        rx.vstack(
            rx.image(src=fetch_random_img()),
            rx.heading("DALL-E", font_size="1.5em"),
            rx.form(
                rx.vstack(
                    rx.input(
                        id="prompt_text",
                        placeholder="Enter a prompt..",
                        size="3",
                    ),
                    rx.button(
                        "Generate Image",
                        type="submit",
                        size="3",
                    ),
                    align="stretch",
                    spacing="2",
                ),
                width="100%",
                # on_submit=State.get_dalle_result,
            ),
            rx.divider(),
            # rx.cond(
            #     State.image_processing,
            #     rx.chakra.circular_progress(is_indeterminate=True),
            #     rx.cond(
            #         State.image_made,
            #         rx.image(
            #             src=State.image_url,
            #         ),
            #     ),
            # ),
            width="25em",
            bg="white",
            padding="2em",
            align="center",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )
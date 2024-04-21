import reflex as rx
from prompted.state import State 


# def fetch_random_img():
#     random_image_filename = random.choice(os.listdir("assets"))
#     return f"/assets/{random_image_filename}"

class CharacterCount(rx.State):
    text: str = "0/50"

    def setCount(self, text):
        self.text = str(len(text)) + "/50"


def game(): 
    # rand_img = fetch_random_img()
    return rx.center(
        rx.vstack(
            rx.image(src=State.promptImg),
            rx.heading("Tell DALL-E to recreate this image.", font_size="1em"),
            rx.heading("You have 50 characters!", font_size="1.5em", color_scheme="ruby"),
            rx.form(
                rx.vstack(
                    rx.hstack(
                        rx.input(
                            id="prompt_text",
                            placeholder="Enter a prompt..",
                            size="3",
                            max_length=50,
                            on_change=CharacterCount.setCount,
                        ),
                        rx.text(
                            CharacterCount.text
                        ),
                        align="center"
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
                on_submit=State.submit_prompt
            ),
            rx.divider(),
            rx.cond(
                State.image_processing,
                rx.chakra.circular_progress(is_indeterminate=True),
                rx.cond(
                    State.image_made,
                    rx.image(
                        src=State.image_url,
                    ),
                ),
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
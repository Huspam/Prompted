import reflex as rx
from prompted.state import State

def index():
    # return
    # Function to render the image selection page
    # images = State.gallery

    # # # Create a list to hold selected images
    # selected_images = []

    # # # Function to handle image selection
    # def select_image(image_url):
    #     nonlocal selected_images
    #     if image_url in selected_images:
    #         selected_images.remove(image_url)
    #     else:
    #         selected_images.append(image_url)

    # # # Generate image elements
    # image_elements = []
    # for image_url in images:
    #     image_element = rx.img(src=image_url, style={"cursor": "pointer"})
    #     image_element.on_click(lambda url=image_url: select_image(url))
    #     image_elements.append(image_element)

    # # # Display selected images
    # selected_image_elements = [rx.img(src=image_url, style={"border": "2px solid blue"}) for image_url in selected_images]

    # Return layout for the image selection page
    # return rx.div(
    #     rx.h1("Image Selection Page"),
    #     rx.div(*image_elements),
    #     rx.h2("Selected Images:"),
    #     rx.div(*selected_image_elements)
    # )
    return rx.center(
        rx.vstack(
            rx.heading("Vote!", font_size="2em"),
            rx.divider(),
            rx.hstack(
                rx.card(
                    rx.image(src=State.promptImg, width="20em", height="auto"),
                    background_color="#111111"
                ),
                rx.divider(orientation="vertical", size="4"),
                rx.form(
                    rx.grid(
                        rx.foreach(
                            State.gallery,
                            lambda img: rx.vstack(
                                rx.card(
                                    rx.image(src=img, width="auto", height="10em",),
                                ),
                                rx.checkbox(
                                ),
                            )
                        ),
                        columns="3",
                        spacing="5",
                        width="100%",
                    ),
                    rx.button(
                        "Place Vote",
                        type="submit",
                        size="3"
                    ),
                    on_submit=State.vote_image
                ),
                spacing="5"
            ),
            height="40em",
            width="70em",
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
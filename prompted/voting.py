import reflex as rx
from prompted.state import State

def voting():
    pass
    # # Function to render the image selection page
    # images = State.get_gallery()

    # # Create a list to hold selected images
    # selected_images = []

    # # Function to handle image selection
    # def select_image(image_url):
    #     nonlocal selected_images
    #     if image_url in selected_images:
    #         selected_images.remove(image_url)
    #     else:
    #         selected_images.append(image_url)

    # # Generate image elements
    # image_elements = []
    # for image_url in images:
    #     image_element = rx.img(src=image_url, style={"cursor": "pointer"})
    #     image_element.on_click(lambda url=image_url: select_image(url))
    #     image_elements.append(image_element)

    # # Display selected images
    # selected_image_elements = [rx.img(src=image_url, style={"border": "2px solid blue"}) for image_url in selected_images]

    # # Return layout for the image selection page
    # return rx.div(
    #     rx.h1("Image Selection Page"),
    #     rx.div(*image_elements),
    #     rx.h2("Selected Images:"),
    #     rx.div(*selected_image_elements)
    # )
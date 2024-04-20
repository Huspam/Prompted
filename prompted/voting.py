import reflex as rx

def generate_image_page():
    # Return layout for the generate image page
    return rx.center(
        rx.heading("Generate Image Page")
        # rx.paragraph("Players can enter a prompt to DALL-E and generate an image.")
    )
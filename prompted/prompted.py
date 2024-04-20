import reflex as rx
from prompted.game import index

# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="medium", accent_color="mint"
    ),
)
app.add_page(index, title="Reflex:DALL-E")

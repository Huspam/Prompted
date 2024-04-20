import reflex as rx
import asyncio

class State(rx.State):
    """The app state."""

    join_made = False
    join_processing = False

    def join_game(self, form_data: dict[str, str]):
        """Join a game session"""
        user_name: str = form_data["user_name"]
        self.join_made = False
        self.join_processing = True
        # Yield here so the image_processing take effects and the circular progress is shown.
        yield
        try:
            # response = get_openai_client().images.generate(
            #     prompt=prompt_text, n=1, size="1024x1024"
            # )
            # self.image_url = response.data[0].url
            self.image_processing = False
            self.image_made = True
            yield
        except Exception as ex:
            self.join_processing = False
            yield rx.window_alert(f"Error with OpenAI Execution. {ex}")
        
    # @rx.background
    # async def get_posts(self):
    #     # Specify the server address here
    #     async with AsyncClient(base_url="http://yourserveraddress.com") as client:
    #         for pid in range(10):
    #             # The URL path here is relative to the base_url specified above
    #             response = await client.get(f"/products/{pid}")
    #             async with self:
    #                 self.posts.append(response.text)
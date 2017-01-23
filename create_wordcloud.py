from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random


class CreateWordCloud:

    def __init__(self, data, width=600, height=600, background="white", background_picture=None,
                 text_style="Sylfaen.ttf", output_name="Unknown_picutre.png"):
        self.data = data
        self.width = width
        self.height = height
        self.img = Image.new("RGB", (self.width, self.height), background)
        self.draw = ImageDraw.Draw(self.img)
        self.text_style = "text_file/" + text_style
        self.output_path = "images/" + output_name
        self.background_picture = background_picture

    # This method create the word cloud :))
    def create_word_cloud(self):

        # If there isn't a background picture, use the background color
        if self.background_picture is None:
            for obj in self.data:
                font = ImageFont.truetype(self.text_style, obj.text_size)

                # draw.text((x, y), text_content, rgb)
                self.draw.text((random.randint(0, self.width - 140), random.randint(0, self.height - 50)),
                                obj.name, obj.color, font)

        else:
            self.img = Image.open(self.background_picture)
            self.draw = ImageDraw.Draw(self.img)

            for obj in self.data:
                font = ImageFont.truetype(self.text_style, obj.text_size)

                # draw.text((x, y), text_content, rgb)
                self.draw.text((random.randint(0, self.width - 140), random.randint(0, self.height - 50)),
                                obj.name, obj.color, font)

        self.img.save(self.output_path)
        print("\n - - - Image successfully created and saved! - - -")

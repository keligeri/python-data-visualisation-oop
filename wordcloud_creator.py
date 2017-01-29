from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random


class WordCloudCreator:
    """This class generate the word cloud. First, the constructor create the neccesary variable. Then the create_word_cloud
       class call two private method, if the user add the background picture, call the __set_the_background_picture,
       else call the drawer private method, which set the font, then draw the words. Finally save the image."""

    def __init__(self, data, width=900, height=900, background="white", background_picture=None,
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
        if self.background_picture is not None:
            self.__set_the_background_picture()

        self.__drawer()
        self.img.save(self.output_path)
        print("\n - - - Image successfully created and saved! - - -")

    def __drawer(self):
        for obj in self.data:
            font = ImageFont.truetype(self.text_style, obj.text_size)
            self.draw.text((random.randint(0, self.width - 140), random.randint(0, self.height - 50)),
                            obj.name, obj.color, font)

    def __set_the_background_picture(self):
        self.img = Image.open(self.background_picture)
        self.draw = ImageDraw.Draw(self.img)

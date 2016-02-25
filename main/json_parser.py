import json

from main.cocktail import Cocktail
from main.glass import Glass

__author__ = 'Albert'


class JsonParser:
    def __init__(self, json_message):
        self.json_message = json_message
        self.cocktail = Cocktail()

    def parse(self):
        message = json.loads(self.json_message)
        glass_key = "glass"
        print glass_key, message[glass_key]
        print
        glass = Glass(message[glass_key], 10)
        self.cocktail.set_glass(glass)
        use_key = "use"
        name_key = "name"
        alcohol_key = "alcohol"
        for i in range(0, 4):
            key = "v" + str(i)
            if message[key][use_key]:
                self.cocktail.setdrink(key, message[key][alcohol_key])
        return self.cocktail

    def get_cocktail(self):
        return self.cocktail

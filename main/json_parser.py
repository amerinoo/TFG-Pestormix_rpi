import json

__author__ = 'Albert'


class JsonParser:
    def __init__(self, json_message):
        self.json_message = json_message

    def parse(self):
        message = json.loads(self.json_message)
        use_key = "use"
        name_key = "name"
        alcohol_key = "alcohol"
        for i in range(0, 4):
            key = "v" + str(i)
            print key
            print message[key][use_key]
            print message[key][name_key]
            print message[key][alcohol_key]
            print

import json

class Export_json():
    def __init__(self,data):
        self.data = data # this is the data you want to export a type dictionary
        with open('record.json', 'w') as outfile:
            json.dump(self.data, outfile)
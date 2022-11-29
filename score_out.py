import json

class Export_json():
    def __init__(self,gamereport):
        #read the json file
        self.gamereport = gamereport

        with open('./data/record.json') as json_file:
            data = json.load(json_file)
        
        data.append(self.gamereport)

         # this is the data you want to export a type dictionary
        with open('./data/record.json', 'w') as outfile:
            json.dump(data, outfile)
            
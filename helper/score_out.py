import json



class Export_json():
    def __init__(self,gamereport):
        '''This function exports the game report to a json file'''
        
        # #read the json file
        with open('./data/record.json') as json_file:
            data = json.load(json_file)

        #json file data ( list of dictionaries )
        self.data = data
        #This is incomeing dictionary data from the game
        self.gamereport = gamereport

        if self.check_exist() == False:
            self.data.append(self.gamereport)
        
         # this is the data you want to export a type dictionary
        with open('./data/record.json', 'w') as outfile:
            json.dump(self.data, outfile)
        
        
    
    def check_exist(self):
        '''
        This function checks if the player name is already in the json file
        if player name exist it will replace the old data with the new data
        only if the time is better and role is the same the data will be replaced

        If player name dont exist it will add the new data to the json file
        '''
        for dict in self.data:
            if dict['name'] == self.gamereport['name'] and dict["role"] == self.gamereport['role'] and dict['time'] > self.gamereport['time']:
                dict.update({"name":self.gamereport['name'],"role":self.gamereport['role'],"time":self.gamereport['time']})
                return True
            elif dict['name'] == self.gamereport['name'] and dict["role"] == self.gamereport['role'] and dict['time'] <= self.gamereport['time']:
                return True
            else:    
                pass
        return False
Export_json({"name": "Jacky", "role": "P1", "time": 10})
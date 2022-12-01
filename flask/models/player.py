import json
import os

class Player():

    def __init__(self) -> None:
        os.chdir("../../Final Project/data/")
        path = os.path.abspath(os.curdir)
        with open(f'{path}/record.json') as json_file:
            data = json.load(json_file)
        self.data = data


    def read_json_out(self):
        return self.data 



    def short_sort_by_time(self,role = None):
        temp = []
        if role != None:
            for dict in self.data:
                if dict["role"] == role:
                    temp.append(dict)
            return sorted(temp, key=lambda x: x["time"], reverse=False)
        else:
            return sorted(self.data, key=lambda x: x['time'],reverse=False)
            

import json
import os


class SeedData:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        file_name = os.path.join(base_dir, 'seeds/seed_data.json')
  
        self.data = json.load(open(file_name))
     

    def categorys(self):
        return self.data["categorys"]

    def sub_categorys(self):
        return self.data["sub_categorys"]

    def users(self):
        return self.data["users"]

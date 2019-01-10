import random

class ServerInfo():
    def __init__(self, *args, **kwargs):
        #self.server_list = ["http://127.0.0.1:3000/", "http://149.28.226.57/"]
        self.server_list = ["http://127.0.0.1:4200/"]
        #self.server_list = ["https://www.google.com"]
        
        self.blacklist = ["xx.xx.xx.xx"]
        #self.blacklist = ["::1"]
        return super().__init__(*args, **kwargs)


    def get_servers(self):
        return self.server_list


    def get_random_server(self):
        return self.server_list[random.randint(0, len(self.server_list)-1)]

    def get_blacklist(self):
        return self.blacklist


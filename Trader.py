class Trader:
    def __init__(self, username):
        self.username = username
        
    def update(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        self._username = value
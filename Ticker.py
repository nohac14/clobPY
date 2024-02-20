class Ticker:
    def __init__(self, identifier):
        self.identifier = identifier
        
    def update(self, identifier):
        self.identifier = identifier
        
    @property
    def identifier(self):
        return self._identifier
    @identifier.setter
    def identifier(self, value):
        self._identifier = value
class Ticker:
    def __init__(self, identifier):
        """
        Initialize a new Ticker with the given identifier.

        :param identifier: The ticker symbol (e.g., 'AAPL' for Apple Inc.)
        """
        self.identifier = identifier
        
    def update(self, identifier):
        """
        Update the ticker identifier.

        :param identifier: The new ticker symbol
        """
        self.identifier = identifier
        
    @property
    def identifier(self):
        """
        Get the ticker identifier.

        :return: The current ticker symbol
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self, value):
        """
        Set the ticker identifier.

        :param value: The new ticker symbol
        """
        self._identifier = value

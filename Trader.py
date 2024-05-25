class Trader:
    def __init__(self, username):
        """
        Initialize a new Trader with the given username.

        :param username: The username of the trader
        """
        self.username = username
        
    def update(self, username):
        """
        Update the trader's username.

        :param username: The new username for the trader
        """
        self.username = username
    
    @property
    def username(self):
        """
        Get the trader's username.

        :return: The current username
        """
        return self._username
    
    @username.setter
    def username(self, value):
        """
        Set the trader's username.

        :param value: The new username
        """
        self._username = value

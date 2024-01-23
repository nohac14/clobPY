from enum import Enum

class Status(Enum):
    OPEN = True
    CANCELED = False
    COMPLETED = -1
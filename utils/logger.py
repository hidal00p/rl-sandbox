import enum

class LogLevel(enum.Enum):
    SILENT = 1
    INFO = 2
    DEBUG = 3
    DEBUG_VERBOSE = 4

class Logger():
    def __init__(self, logLevel: LogLevel = LogLevel.DEBUG):
        assert isinstance(logLevel, LogLevel), "Please provide logLevel param if type LogLevel"
        
        self.logLevel = logLevel
        self.logBuffer = []

    """
    Stores data that would want to be examined.
    Please provide a data structure that is responsible for compacting and displaying data.
    This data strcture should also override __str__ signature
    """
    def store(self, objToStore):
        self.logBuffer.append(objToStore)
    
    def log(self, info: str):
        print(f"[{self.logLevel.name}]: {info}")
    
    def logAll(self):
        #TODO: add object analyzer that generates overall data about the set of stored objects
        
        self.log("Dumping collected buffer!")
        for obj in self.logBuffer:
            print(obj)
        
        # Reset buffer
        self.logBuffer = []
    
    
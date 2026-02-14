# Ensures that only one instance of a class is created and provides a global point of access to that instance.

# When to use Singleton Pattern:

# Database connection
# Logger
# Configuration manager
# Cache
# Thread pool
class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print(f"Creating new instance of Logger: {cls._instance}")
        return cls._instance
    def log(self, message: str):
        print(f"Log: {message}")


logger1 = Logger()
logger2 = Logger()

logger1.log("This is a log message.")
print( logger1 is logger2)

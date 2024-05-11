from kivy.logger import Logger

class CAN(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path : str)
        self.open(config_path)

    def open(self, config_path : str):
        self.config_path = config_path
        if not self.is_open:
            Logger.info(f"CAN : config {self.config_path} Open")
            self.is_open = True
        else:
            Logger.error(f"CAN : config {self.config_path} already Opened")

    def close(self):
        if self.is_open:
            Logger.info(f"CAN : Config {self.config_path} Closed")

    def __del__(self):
        self.close()

    def send(message : str = "") -> bool:
        if not self.is_open:
            Logger.error(f"CAN : No port opened")
            return False

        Logger.info(f"CAN : {self.config_path} : sent {messge}")
        return True

    def receive()->str:
        message : str = "hoghoge"
        Logger.info(f"CAN : {self.config_path} : receive {messge}")
        return message

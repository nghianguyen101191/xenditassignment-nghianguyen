from utils.manage_util import Driver


class DriverManager:
    def start_driver(self, name="chrome"):
        return Driver().create_driver(name)
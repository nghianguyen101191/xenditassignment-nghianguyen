from utils.driver_manager import DriverManager

__driver = {}

class Key:
    current = "default"
def start_driver(name, driver_key="default"):
    driver = DriverManager().start_driver(name)
    __driver[driver_key] = driver
    Key.current = driver_key

def get_driver():
    try:
        return __driver[Key.current]
    except:
        return None
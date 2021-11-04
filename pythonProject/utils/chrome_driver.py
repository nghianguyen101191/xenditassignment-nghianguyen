from utils import factory

def start_driver(name="chrome", key="default"):
    factory.start_driver(name, key)


def get_driver():
    return factory.get_driver()


def maximize_browser():
    get_driver().maximize_window()

def take_screen_shot():
    return get_driver().get_screenshot_as_png()
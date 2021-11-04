from utils.element_methods import ElementMethod
from util_page import UtilPage
from constants import constant


class CalculatePage(UtilPage):
    def __init__(self):
        super().__init__()
        self.iframe_fullframe = ElementMethod("xpath=//iframe[@id='fullframe']")
        self.canvas_calculator = ElementMethod("xpath=//canvas[@id='canvas']")

    def open_calculator_page(self):
        self.open_url(constant.URL["calculator_page"])

    def switch_to_fullframe(self):
        self.iframe_fullframe.switch_to_iframe()

    def switch_to_default_frame(self):
        self.iframe_fullframe.switch_to_default_iframe()

    def send_keys_on_canvas(self, key_value):
        self.canvas_calculator.send_keys_action(key_value=key_value)

    def take_calculated_result_screenshot(self):
        return self.canvas_calculator.take_screenshot()

from behave import given, when, then, register_type
import parse
from tests.pages.calculate_page import CalculatePage
from utils import osr

CalculatePage = CalculatePage()



@given('I open Calculator Page')
def open_calculator_page_step():
    CalculatePage.open_calculator_page()


@when(r'I switch to default full iframe')
def switch_to_iframe_fullframe():
    CalculatePage.switch_to_fullframe()


@then(r'I switch to default iframe')
def switch_to_default_iframe():
    CalculatePage.switch_to_default_frame()


@when(r'I input operator into Calculator = "{canbe null}"')
def send_keys_to_calculator(key_value):
    CalculatePage.send_keys_on_canvas(key_value=key_value)


@then(r'It should be shown result "{canbe null}"')
def take_calculator_screenshot(expected_result):
    screenshot_path = CalculatePage.take_calculated_result_screenshot()
    actual_result = osr.get_ocr_text(screenshot_path)
    assert actual_result == str(expected_result), "Actual Result = " + actual_result + " != " + "Expected Result = " + expected_result

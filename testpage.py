import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class Operations(BasePage, TestLocators):

    # ENTER TEXT
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} nit found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def enter_login(self, word):
        self.enter_text_into_field(TestLocators.ids["field_login"], word, description="Login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestLocators.ids["field_passwd"], word, description="Password form")

    # CLICK
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def click_login_button(self):
        self.click_button(TestLocators.ids["btn_selector"], description="login")

    def click_about(self):
        self.click_button(TestLocators.ids["btn_about"], description="contact us")

    # GET TEXT
    def get_text_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_error_hello(self):
        return self.get_text_element(TestLocators.ids["text_hello_user"])

    def get_error_about(self):
        return self.get_text_element(TestLocators.ids["text_about"])

    def get_text_about(self):
        about_page_field = self.find_element(TestLocators.ids['text_about'], time=3)
        font = about_page_field.value_of_css_property('font-size')
        return font



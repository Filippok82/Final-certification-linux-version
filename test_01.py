import logging
import time
import yaml
from BaseApp import BasePage
from testpage import Operations
from post import send_mail

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step01(browser):
    logging.info("Test1 Starting")
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login(testdata["login"])
    page.enter_pass(testdata["passwd"])
    page.click_login_button()
    time.sleep(testdata["sleep_time"])
    assert page.get_error_hello() == "Hello, {}".format(testdata["login"])


def test_step02(browser):
    logging.info("Test2 Starting")
    page = Operations(browser)
    page.click_about()
    time.sleep(testdata["sleep_time"])
    assert page.get_error_about() == testdata["text_about"]


def test_step03(browser):
    logging.info("Test3 Starting")
    page = Operations(browser)
    time.sleep(testdata["sleep_time"])
    assert page.get_text_about() == testdata["size_title"]
    send_mail()



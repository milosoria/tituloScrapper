from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from typing import List
from sys import stdout


class WebScrapper:
    def __init__(self, url: str):
        self.url = url
        # TODO: fix this hardcoded path to make it portable to all OS
        self.driver = webdriver.Chrome(
            "/usr/lib/chromium-browser/chromedriver")
        self.courses_list = []
        self.course_searched = None

    def load_page(self) -> None:
        stdout.write("WebScrapper@load_page: Loading page...\n")
        self.driver.get(self.url)

    def send_input(self,
                   input: str,
                   strategy: str = "",
                   input_identifier: str = "") -> None:
        self.course_searched = input
        stdout.write("WebScrapper@send_input: Sending input...\n")
        try:
            if strategy == "id":
                input_field =self.driver.find_element_by_id(input_identifier)
            elif strategy == "name":
                input_field = self.driver.find_element_by_name(input_identifier)
            elif strategy == "class_name":
                input_field = self.driver.find_element_by_class_name(
                    input_identifier)
            else:
                # default to xpath hardcoded
                input_field = self.driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td/div/div/div/div[2]/div[1]/div/div[4]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/input")
            input_field.clear()
            input_field.send_keys(input)
        except NoSuchElementException as e:
            stdout.write(
                "WebScrapper@send_input: The following error ocurred when finding element and sending keys:\n"
                % str(e))

    def submit(self, strategy: str = "", button_identifier: str = "") -> None:
        stdout.write("WebScrapper@submit: Submitting info...\n")
        try:
            if strategy == "id":
                btn = self.driver.find_element_by_id(button_identifier)
            elif strategy == "class_name":
                # default to xpath hardcoded
                btn = self.driver.find_element_by_class_name(button_identifier)
            else:
                # TODO: how to do this, without hardcoding it. Maybe with input through the terminal
                btn = self.driver.find_element_by_xpath(
                    '/html/body/table/tbody/tr/td/div/div/div/div[2]/div[1]/div/div[4]/div/div[2]/div/form/input[1]'
                )
            stdout.write("WebScrapper@submit: clicking...\n")
            btn.click()
        except NoSuchElementException as e:
            stdout.write(
                "WebScrapper@submit: The following error ocurred when finding element and submitting:\n"
                % str(e))

    def check_existance(self, class_name: str) -> bool:
        # TODO: fix this
        try:
            self.driver.find_element_by_class_name(class_name)
        except NoSuchElementException as e:
            stdout.write(
                "WebScrapper@submit: The following error ocurred when finding element and submitting:\n"
                % str(e))
            return False
        finally:
            return True

    def finish(self) -> None:
        self.driver.close()

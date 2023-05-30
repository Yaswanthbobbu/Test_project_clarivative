from page_object_model.base_page import BasePage
from locators.page_locators import *
from page_object_model.base_element import *


class ProQuest(BasePage):

    def search_input(self):
        return BaseElement(self.driver, search_input)

    def titles(self):
        return BaseElement(self.driver, titles_locator).find_all()

    def proquest_search_input(self):
        return BaseElement(self.driver, proquest_search_input_locator)

    def manage_cookies(self):
        return BaseElement(self.driver, cookies_locator)

    def proquest_search_button(self):
        return BaseElement(self.driver, proquest_search_button_locator)




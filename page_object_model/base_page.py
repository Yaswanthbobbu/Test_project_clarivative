from page_object_model.base_element import *


class BasePage():
    def __init__(self, driver):
        self.driver = driver


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import *


class BaseElement:
    def __init__(self, driver, locator, web_element= None, wait=5, check_existence=False):
        self.driver = driver
        self.locator = locator
        self.web_element = web_element
        self.wait = wait
        if not check_existence:
            self.find()

    def find(self):
        try:
            element = WebDriverWait(self.driver, self.wait).until(
                EC.presence_of_element_located(locator=self.locator)
            )
            self.web_element = element
        except:
            raise TimeoutError("The web element with locator [{}] is either not present or is not ready yet".format(self.locator))

        return None

    def find_all(self):
        web_elements = WebDriverWait(self.driver, self.wait).until(
            EC.presence_of_all_elements_located(locator=self.locator)
        )
        elements = list()
        for element in web_elements:
            element = BaseElement(self.driver, self.locator, web_element=element, check_existence=True)
            elements.append(element)
        return elements

    def find_visible_element(self):
        element = WebDriverWait(self.driver, self.wait).until(
            EC.visibility_of_any_elements_located(locator=self.locator)
        )
        self.web_element = element[0]
        return self

    def find_children(self, locator):
        web_elements = self.web_element.find_elements(*locator)
        elements = list()
        for element in web_elements:
            element = BaseElement(self.driver, self.locator, web_element=element, check_existence=True)
            elements.append(element)
        return elements

    def enter_text(self, txt):
        self.web_element.clear()
        self.web_element.send_keys(txt)
        return None

    @property
    def text(self):
        text = self.web_element.text.replace('\xad', '')
        return text

    def submit(self):
        return self.web_element.submit()

    def click(self,x=None,y=None):
        if len(self.driver.find_elements(*self.locator)) == 1:
            element = WebDriverWait(self.driver, self.wait).until(
                EC.element_to_be_clickable(self.locator)
            )
            if x:
                handle = ActionChains(self.driver)
                handle.move_to_element_with_offset(element,x,y)
                handle.click()
                handle.perform()
            else:
                element.click()
        else:
            self.web_element.click()
        return None

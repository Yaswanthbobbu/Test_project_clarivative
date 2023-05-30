import os
import platform
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from page_object_model.web_page import ProQuest


def before_feature(context, feature):
    BROWSER = context.config.userdata.get("browser")

    if platform.system() == 'Windows':
        if BROWSER == 'Chrome':
            context.driver = webdriver.Chrome(ChromeDriverManager().install())
            context.driver.maximize_window()
    elif platform.system() == 'Linux':
        if BROWSER == 'Chrome':
            context.driver = webdriver.Chrome(ChromeDriverManager().install())
            context.driver.maximize_window()

    feature.web_page = ProQuest(context.driver)
    feature.page = context.feature.web_page


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    context.driver.quit()

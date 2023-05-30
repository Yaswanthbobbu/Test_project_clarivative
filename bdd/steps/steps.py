import os
from utilities.utility_functions import *
from behave import *


@given('user launches the Google search page')
def step_impl(context):
    context.driver.get('https://www.google.com')


@when('he enters "{search_term}" and hits enter')
def step_impl(context, search_term):
    search_bar = context.feature.page.search_input()
    search_bar.enter_text(search_term)
    search_bar.submit()


@step('he captures all titles from the webpage')
def step_impl(context):
    titles = context.feature.page.titles()
    context.titles = [title.text for title in titles if title.text]


@then('the user saves the titles in a text file')
def step_impl(context):
    folder_path = 'results'
    file_path = os.path.join(folder_path, "capture_titles.txt")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, 'w') as file:
        file.write('\n'.join(context.titles))


@given('user opens "{website}" website')
def step_impl(context, website):
    context.driver.get("https://www.proquest.com/")
    context.driver.maximize_window()


@when('user searches for "{search}" in the top navigation')
def step_impl(context, search):
    search_box = context.feature.page.proquest_search_input()
    if context.feature.page.manage_cookies():
        context.feature.page.manage_cookies().click()
    search_box.enter_text(search)
    search_button = context.feature.page.proquest_search_button()
    search_button.click()


@then('user captures the screenshot of the search page')
def step_impl(context):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    screenshot_path = os.path.join("screenshots", "screenshot.png")
    snooze(2)
    context.driver.save_screenshot(screenshot_path)
    snooze(2)

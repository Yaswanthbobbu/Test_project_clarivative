# BDD Framework

This is a BDD (Behavior-Driven Development) framework for automating scenarios using Selenium and Gherkin syntax.

# Setup

The test are written in Python language and requires an active installation of Python 3.8.

# Installation

1. `pip install --upgrade pip --user`

2. `pip install -r requirements.txt`

# Browser

1. Open `./behave.ini`

2. Change the value for browser parameter as per you choice of browser to run the tests. 
   Following values are accepted: `Chrome`,`Firefox`
3. 
3. Set up the appropriate browser driver for Selenium (e.g., ChromeDriver) and make sure it's in your system's PATH.

## Usage

1. Define your scenarios using Gherkin syntax in the feature files located in the `features` directory.

2. Implement the step definitions for the scenarios in the `step_definitions` directory.

3. Execute the BDD tests using the following command:


The framework will automatically discover and execute the feature files along with their corresponding step definitions. The browser will open, perform the defined steps using Selenium, take a screenshot, and then close the browser. The screenshots will be saved in the `screenshots` directory.

## Project Structure

- `features`: Contains the feature files written in Gherkin syntax.
- `step_definitions`: Contains the step definitions implemented in Python.
- `screenshots`: Stores the screenshots taken during the test execution.
- `utils.py`: Provides utility functions used by the framework.



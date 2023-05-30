from selenium.webdriver.common.by import By

routing_title_container_locator = (By.CSS_SELECTOR, ".routing-tile>span.web-app")
search_input = (By.NAME, 'q')
titles_locator = (By.CSS_SELECTOR, ".LC20lb")  #h3

proquest_search_input_locator = (By.ID, "searchTerm")
cookies_locator = (By.ID, 'onetrust-close-btn-container')
proquest_search_button_locator = (By.ID, "expandedSearch")

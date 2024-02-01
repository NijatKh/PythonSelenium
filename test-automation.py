import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTest(unittest.TestCase):
    def setUp(self):
        # Initializing the WebDriver. Example for Chrome.
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Closing the WebDriver session.
        self.driver.quit()

class SearchTest(BaseTest):
    def test_search(self):
        search_engines = {
            "Google": "https://www.google.com",
            "Bing": "https://www.bing.com",
            "Yahoo": "https://www.yahoo.com"
        }
        search_term = "42"
        for name, url in search_engines.items():
            with self.subTest(search_engine=name):
                self.search_and_assert(url, search_term)

    def search_and_assert(self, url, term):
        driver = self.driver
        driver.get(url)

        # search engine, search box element;
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(term + Keys.RETURN)

        # Wait for the results to load and assert the first result.
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        self.assertIsNotNone(first_result, "No results found.")

if __name__ == "__main__":
    unittest.main()

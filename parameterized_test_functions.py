from selenium import webdriver


class TestClass:

    def setup(self):
        # Test variables
        # super().setup()
        self.test_url = 'https://lambdatest.com/'
        self.expected_title = "Most Powerful Cross Browser Testing Tool Online" \
                              " | LambdaTest"

        # Driver initialization
        self.web_driver = webdriver.Chrome()

    def teardown(self):
        # Close driver
        # super().teardown()
        self.web_driver.close()

    def test_check_title_1(self):
        self.web_driver.get(self.test_url)
        self.web_driver.maximize_window()
        assert self.expected_title == self.web_driver.title


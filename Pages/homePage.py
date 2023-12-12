from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    label_product_xpath = "//span[@class='title'][contains(.,'Products')]"

    def __init__(self, driver):
        self.driver = driver

    # def enterUsername(self, username):
    #     wait = WebDriverWait(self.driver, 30)
    #     element = wait.until(EC.visibility_of_element_located((By.ID, self.textbox_username_id)))
    #     element.send_keys(username)

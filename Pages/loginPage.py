from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    label_loginError_xpath = "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.textbox_username_id)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id)))
        element.send_keys(password)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.button_login_id)))
        element.click()

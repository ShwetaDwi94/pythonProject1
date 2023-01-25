from selenium import webdriver

class Login:
    username_id = "Email"
    password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    button_logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("id", "Email").clear()
        self.driver.find_element("id", "Email").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("id", "Password").clear()
        self.driver.find_element("id", "Password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", "//button[text()='Log in']").click()

    def clickLogout(self):
        self.driver.find_element("xpath", "//a[text()='Logout']").click()
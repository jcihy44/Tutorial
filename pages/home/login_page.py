from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[contains(text(),'Sign In')]"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="ID")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
	    # time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        # result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
        #                                locatorType="xpath")
        # return result
        self.waitForElement("//div[@id = 'navbar-inverse-collapse']", locatorType="xpath")
        result = self.isElementPresent(locator="//span[contains(text(), 'My Account')]")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details')]",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyTitle(self):
        if "Google" in self.getTitle():
            return True
        else:
            return False



from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = "#email"
    PASSWORD = "#password"
    LOGIN = "#login-btn"

    def login(self, email, password):

        self.page.fill(self.EMAIL, email)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN)

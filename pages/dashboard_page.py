from pages.base_page import BasePage

class DashboardPage(BasePage):

    WELCOME = ".welcome-message"

    PROJECTS = ".project-card"

    def is_dashboard_loaded(self):

        return self.page.locator(self.WELCOME).is_visible()

    def get_projects(self):

        return self.page.locator(self.PROJECTS)

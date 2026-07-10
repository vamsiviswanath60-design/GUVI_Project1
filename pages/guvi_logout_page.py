from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):

    PROFILE_ICON = (By.XPATH, "(//img[@class='rounded-full gravatar w-8 h-8'])[1]")
    LOGOUT_BUTTON = (By.XPATH, "//p[text()='Sign Out']")

    def click_profile(self):
        self.js_click(self.PROFILE_ICON)

    def click_logout(self):
        self.js_click(self.LOGOUT_BUTTON)
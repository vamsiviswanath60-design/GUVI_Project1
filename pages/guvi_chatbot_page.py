from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChatbotPage(BasePage):

    CHATBOT_ICON = (By.XPATH, "//span[@aria-label='Chat Widget']")
    CHATBOT_IFRAME = (By.ID, "siq_chatwindow")
    MINI_TEXT = (By.XPATH, "//div[text()='Mini']")

    def click_chatbot(self):
        self.click(self.CHATBOT_ICON)

    def switch_to_chatbot_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.CHATBOT_IFRAME))

    def is_mini_visible(self):
        return self.is_element_visible(self.MINI_TEXT)
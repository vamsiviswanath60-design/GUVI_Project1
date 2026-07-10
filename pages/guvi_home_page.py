from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.config import BASE_URL


class GuviHomePage(BasePage):

    LOGIN_BUTTON = (By.ID, "login-btn")
    SIGNUP_BUTTON = (By.XPATH, "(//button[text()='Sign up'])[1]")
    EMAIL_TEXTBOX = (By.XPATH, "(//input[@type='email'])[1]")
    PASSWORD_TEXTBOX = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//a[@id='login-btn']")
    ENROLL_NOW_BUTTON = (By.XPATH, "(//span[text()='Enroll Now'])[2]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(),'Incorrect')]")
    COURSES_MENU = (By.XPATH, "(//p[text()='Courses'])[1]")
    LIVE_CLASSES_MENU = (By.XPATH, "(//p[text()='LIVE Classes'])[1]")
    PRACTICE_MENU = (By.XPATH, "(//p[text()='Practice'])[1]")

    def open_home_page(self):
        self.open_url(BASE_URL)

    def get_home_page_title(self):
        return self.get_title()

    def is_login_button_visible(self):
        return self.is_element_visible(self.LOGIN_BUTTON)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def is_signup_button_visible(self):
        return self.is_element_visible(self.SIGNUP_BUTTON)

    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_TEXTBOX, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_TEXTBOX, password)

    def click_login(self):
        self.click(self.LOGIN_SUBMIT_BUTTON)

    def is_enroll_now_visible(self):
        return self.is_element_visible(self.ENROLL_NOW_BUTTON)

    def is_error_message_visible(self):
        return self.is_element_visible(self.ERROR_MESSAGE)

    def is_courses_visible(self):
        return self.is_element_visible(self.COURSES_MENU)

    def is_live_classes_visible(self):
        return self.is_element_visible(self.LIVE_CLASSES_MENU)

    def is_practice_visible(self):
        return self.is_element_visible(self.PRACTICE_MENU)
from pages.guvi_home_page import GuviHomePage
from pages.guvi_chatbot_page import ChatbotPage


def test_09_verify_dobby_assistant(driver):

    home_page = GuviHomePage(driver)

    chatbot_page = ChatbotPage(driver)

    home_page.open_home_page()

    chatbot_page.click_chatbot()

    chatbot_page.switch_to_chatbot_frame()

    assert chatbot_page.is_mini_visible()
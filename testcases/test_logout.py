from pages.guvi_home_page import GuviHomePage
from pages.guvi_logout_page import LogoutPage
import time


def test_10_verify_logout(driver):

    home_page = GuviHomePage(driver)

    logout_page = LogoutPage(driver)

    home_page.open_home_page()

    home_page.click_login_button()

    home_page.enter_email("vamsiviswanath60@gmail.com")

    home_page.enter_password("aspirineAS1@")

    home_page.click_login()

    time.sleep(2)

    logout_page.click_profile()

    time.sleep(2)

    logout_page.click_logout()

    assert "https://www.guvi.in/" == driver.current_url
from pages.guvi_home_page import GuviHomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import BASE_URL


# ---------------------------------------------------------
# TC-01: Verify Home Page URL
# ---------------------------------------------------------
def test_01_verify_home_page_url(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    assert BASE_URL in driver.current_url


# ---------------------------------------------------------
# TC-02: Verify Home Page Title
# ---------------------------------------------------------
def test_02_verify_home_page_title(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    expected_title = "HCL GUVI | Learn to code in your native language"

    assert home_page.get_home_page_title() == expected_title


# ---------------------------------------------------------
# TC-03: Verify Login Button
# ---------------------------------------------------------
def test_03_verify_login_button(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    assert home_page.is_login_button_visible()

    home_page.click_login_button()

    WebDriverWait(driver, 5).until(
        EC.url_contains("sign-in")
    )

    assert "sign-in" in driver.current_url.lower()


# ---------------------------------------------------------
# TC-04: Verify Sign Up Button
# ---------------------------------------------------------
def test_04_verify_signup_button(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    assert home_page.is_signup_button_visible()

    home_page.click_signup_button()

    WebDriverWait(driver, 5).until(
        EC.url_contains("register")
    )

    assert "register" in driver.current_url.lower()


# ---------------------------------------------------------
# TC-05: Verify Sign Up Page URL
# ---------------------------------------------------------
def test_05_verify_signup_page(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    home_page.click_signup_button()

    WebDriverWait(driver, 5).until(
        EC.url_contains("register")
    )

    assert "https://www.guvi.in/register/" in driver.current_url.lower()


# ---------------------------------------------------------
# TC-06: Verify Valid Login
# ---------------------------------------------------------
def test_06_verify_valid_login(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    home_page.click_login_button()

    home_page.enter_email("vamsiviswanath60@gmail.com")

    home_page.enter_password("aspirineAS1@")

    home_page.click_login()

    assert home_page.is_enroll_now_visible()


# ---------------------------------------------------------
# TC-07: Verify Invalid Login
# ---------------------------------------------------------
def test_07_verify_invalid_login(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    home_page.click_login_button()

    home_page.enter_email("invalid@gmail.com")

    home_page.enter_password("WrongPassword123")

    home_page.click_login()

    assert home_page.is_error_message_visible()


# ---------------------------------------------------------
# TC-08: Verify Menu Items
# ---------------------------------------------------------
def test_08_verify_menu_items(driver):

    home_page = GuviHomePage(driver)

    home_page.open_home_page()

    assert home_page.is_courses_visible()

    assert home_page.is_live_classes_visible()

    assert home_page.is_practice_visible()
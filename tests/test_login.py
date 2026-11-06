from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_valid(home_page, login_page, test_data_reader):
    user_name = test_data_reader["login"]["name"]
    email = test_data_reader["login"]["email"]

    home_page.click_signup_tab()
    login_page.login(user_name, email)
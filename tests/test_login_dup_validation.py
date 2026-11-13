import pytest
import random
import string

def generate_random_email():
    username = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=8)
    )
    return f"{username}@gmail.com"

@pytest.mark.regression
def test_login_validation(home_page,login_page,signup_page, test_data_reader):
    home_page.click_signup_tab()
    user_name = test_data_reader["login"]["name"]
    email = generate_random_email()
    login_page.login(user_name,email)
    assert signup_page.is_account_info_exists() == True, "The message Enter account information does not exist"


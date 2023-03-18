import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():

    def __init__(self, driver_g):
        self.driver_g = driver_g
    def authorization(self, login_name, login_password, count):

        user_name = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print("Input Login " + str(count))

        time.sleep(0.5)
        password = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(login_password)
        print("Input Password")

        time.sleep(0.5)
        button_login = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print("Click Login Button")
        time.sleep(1)

    def logout(self, login_name):
        success_test = WebDriverWait(self.driver_g, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == "Products"
        print("Assert Page is Correct")
        time.sleep(1)

        menu_button = WebDriverWait(self.driver_g, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        menu_button.click()
        print("Click Menu Button")
        time.sleep(1)
        logout_button = WebDriverWait(self.driver_g, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_button.click()
        print("Click Logout Button")
        success_back = WebDriverWait(self.driver_g, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='login_logo']")))
        value_success_back = success_back.text
        assert value_success_back == "Swag Labs"
        print("Assert Page is Correct")
        print("Test for " + login_name + " is Successful!!!")

    def authorization_error(self, login_name):
        error_message = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//h3[@data-test='error']")))
        value_error_message = error_message.text
        assert value_error_message == "Epic sadface: Sorry, this user has been locked out."
        print("Assert Error Message is Correct")
        time.sleep(0.5)

        close_error = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='error-button']")))
        close_error.click()
        print("Error Message Closed")
        print("Test for " + login_name + " is Successful!!!")
        time.sleep(0.5)

        user_name = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(Keys.CONTROL + "A")
        user_name.send_keys(Keys.BACKSPACE)
        print("Login Field Empty")

        time.sleep(0.5)
        password = WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(Keys.CONTROL + "A")
        password.send_keys(Keys.BACKSPACE)
        print("Password Field Empty")





import time
from collections import deque
from selenium import webdriver
from login_page import Login_page


class Test_1():

    def test_login_list(self):
        driver_g = webdriver.Chrome('C:\\Users\\NadyaDexter\\PycharmProjects\\resource\chromedriver.exe')
        base_url = 'https://www.saucedemo.com/'
        driver_g.get(base_url)
        driver_g.maximize_window()

        print("Start Test")

        login_standard_user = deque(["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"])
        password_all = "secret_sauce"
        test_count = 0
        try:
            while True:
                login = Login_page(driver_g)
                user_name = login_standard_user.popleft()
                test_count = test_count + 1
                login.authorization(user_name,  password_all, test_count)

                try:
                    login.logout(user_name)
                except:
                    login.authorization_error(user_name)
                else:
                    login = Login_page(driver_g)
                    user_name = login_standard_user.popleft()
                    test_count = test_count + 1
                    login.authorization(user_name, password_all, test_count)
                    try:
                        login.logout(user_name)
                    except:
                        login.authorization_error(user_name)
        except IndexError:
            print("Test Over")
        time.sleep(3)

test = Test_1()
test.test_login_list()
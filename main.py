import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By



driver: WebDriver = webdriver.Chrome(executable_path=r'XXXX') #путь к драйверу

class Test_Yandex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Тестирование выполняется...')

    def test_log_in(self):
        print(driver.title)

        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(By.NAME, "login")
        elem.send_keys("ХХХ") #Вставить логин

        time.sleep(2)
        login_button = driver.find_element(By.ID, "passp:sign-in")
        login_button.click()
        time.sleep(2)
        passwd_elems = driver.find_elements(By.NAME, 'passwd')
        self.assertTrue(len(passwd_elems) > 0)

        passwd_elems[0].send_keys("хххххх") #Вставить пароль

        login_button1 = driver.find_element(By.ID, "passp:sign-in")
        login_button1.click()
        time.sleep(2)

        self.assertTrue(driver.title == 'Яндекс ID')

    @classmethod
    def tearDownClass(cls):
        print('Тестирование завершено')

if __name__ == '__main__':
    Test_Yandex()

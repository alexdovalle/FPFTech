from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class User:
    def create_driver(self):
        self.drive = webdriver.Chrome()
        
    def test_search_in_automation_exercise(self):
        driver = self.drive
        driver.get('https://automationexercise.com/')
        elem = driver.find_element(By.CLASS_NAME, 'fa.fa-lock')
        elem.click()
        elem = driver.find_element(By.NAME, 'name')
        elem.send_keys('Alexandre')
        elem = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
        elem.send_keys('emaildoalexandre@email.com')
        elem.send_keys(Keys.RETURN)
        input(' Para ai mano')
        
    def tearDown(self):
        self.drive.close()

if __name__ == '__main__':
    user = User()
    user.create_driver()
    user.test_search_in_automation_exercise()
    
    

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
        elem = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/div[1]/div[1]/label/div')
        elem.click()
        elem = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/div[4]/input')
        elem.send_keys('senhadoalexandre')
        select_days = Select(driver.find_element(By.ID, 'days'))
        select_days.select_by_value('5')
        select_months = Select(driver.find_element(By.ID, 'months'))
        select_months.select_by_value('7')  
        select_year = Select(driver.find_element(By.ID, 'years'))
        select_year.select_by_value('1993')  
        elem = driver.find_element(By.NAME, 'newsletter')
        elem.click()
        elem = driver.find_element(By.NAME, 'optin')
        elem.click()
        elem = driver.find_element(By.NAME, 'first_name')
        elem.send_keys('Alexandre')
        elem = driver.find_element(By.NAME, 'last_name')
        elem.send_keys('Tech')
        elem = driver.find_element(By.NAME, 'company')
        elem.send_keys('FPFTech')
        elem = driver.find_element(By.NAME, 'address1')
        elem.send_keys('Rua 1')
        elem = driver.find_element(By.NAME, 'address2')
        elem.send_keys('Rua 2')
        select_pais = Select(driver.find_element(By.ID, 'country'))
        select_pais.select_by_value('United States')
        elem = driver.find_element(By.NAME, 'state')
        elem.send_keys('New York')
        elem = driver.find_element(By.NAME, 'city')
        elem.send_keys('New York')
        elem = driver.find_element(By.NAME, 'zipcode')
        elem.send_keys('12345')
        elem = driver.find_element(By.NAME, 'mobile_number')
        elem.send_keys('1234567890')
        elem = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/button')
        elem.click()
        elem = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/a')
        elem.click()
        elem = driver.find_element(By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[5]/a')
        elem.click()
        elem = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/a')
        elem.click()
        input('Digite algo aqui meu amigo: ')



        print('Sábias palavras, flww')
    def tearDown(self):
        self.drive.close()

if __name__ == '__main__':
    user = User()
    user.create_driver()
    user.test_search_in_automation_exercise()
    
    

import email
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#prefix = bir kelimenin önüne gelecek kalıp
#class için= Test_...
#fonksiyonlar için= test_...
# annotation = 
# assert => test sonucunun bağlı olduğu condition
class Test_kodlamaio:
    #setup_method => her test öncesi çalışır. ön kurulum methodudur
    def setup_method(self):
        self.driver = webdriver.Chrome()
    #teardown_method => her test bitiminde çalışır. temizlik methodu
    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skipt
    @pytest.mark.parametrize("username,password",[("halit","halit"),("engin","engin"),("ahmet","ahmet")])
    def test_login(self,username,password):
        assert username==password
    
    @pytest.mark.parametrize("username,password",[("ddd@d.com","123123"),("sadlas@d.com","123")])
    def test_invalid_login(self,username,password):
        expected_message = "Your email or password is incorrect."
        self.driver.get("https://www.kodlama.io/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="navbar"]/div/div/div/ul/li[3]/a')))
        loginBtn = self.driver.find_element(By.XPATH,'//*[@id="navbar"]/div/div/div/ul/li[3]/a')
        loginBtn.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,'email')))
        emailInput = self.driver.find_element(By.ID,'email')
        emailInput.send_keys(username)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,'password')))
        passwordInput = self.driver.find_element(By.ID,'password')
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'auth-flash-error')))
        errorLabel = self.driver.find_element(By.CLASS_NAME,"auth-flash-error")
        assert errorLabel.text.strip() == expected_message

    @pytest.mark.skip
    def test_register(self):
        assert 3==3


class Test_KodlamaIoRegister:
    def test_register(self):
        assert 2==2

# ödev => 3 test case belirlenecek (en az 1'i parametrik) pytest ve selenium ile birlikte
# testler otomasyona bağlanacak
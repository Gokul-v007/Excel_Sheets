from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_js_alert():
    driver = webdriver.Chrome()

    #Text Box Test Case

    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.ID,"userName").send_keys("Gokul V")
    time.sleep(3)
    driver.find_element(By.ID,"userEmail").send_keys("gokulnklv@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID,"currentAddress").send_keys("Karpagam Institute of Technology is S.F.No.247,248, L&T Bypass Road, Seerapalayam Village, Bodipalayam Post, Coimbatore – 641 105, Tamil Nadu, India")
    time.sleep(3)
    driver.find_element(By.ID,"permanentAddress").send_keys("Karpagam Institute of Technology is S.F.No.247,248, L&T Bypass Road, Seerapalayam Village, Bodipalayam Post, Coimbatore – 641 105, Tamil Nadu, India")
    time.sleep(3)
    driver.find_element(By.ID,"submit").click()
    time.sleep(5)


    #CheckBox Test Case

    driver.get("https://demoqa.com/checkbox")
    driver.find_element(By.XPATH, "//span[contains(@class,'rct-checkbox')]").click()
    time.sleep(5)

    #Radio Buttom Test Case
    
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    time.sleep(3)


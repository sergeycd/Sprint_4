import random
import time

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
import PageObject.Informations
from PageObject.locators import *
from PageObject.Pages import ActionOnPage
from PageObject.Informations import TextInfo

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://qa-scooter.praktikum-services.ru/order")

driver.find_element(*MainPageLocators.BUTTON_ACCEPT_COOKIES).click()

driver.find_element(*OrderPageLocators.FIELD_NAME).send_keys("Евгений")
driver.find_element(*OrderPageLocators.FIELD_LAST_NAME).send_keys("Греков")
driver.find_element(*OrderPageLocators.FIELD_ADDRESS_WHERE_TO_TAKE).send_keys("Новосибирск")
driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER).send_keys("89607807555")
bootstrap = driver.find_element(*OrderPageLocators.BOOTSTRAP)
bootstrap.send_keys("Сокольники")
bootstrap.send_keys(Keys.ARROW_DOWN + Keys.ENTER)


driver.find_element(*OrderPageLocators.NEXT).click()

#

driver.find_element(*AboutRentLocators.WHEN_TO_BRING).send_keys("23.10.2022")

index = random.randint(0, 6)
color = random.randint(0, 1)
driver.find_element(*AboutRentLocators.DROPDOWN_ARROW).click()
driver.find_elements(*AboutRentLocators.DROPDOWN_MENU)[6].click()

driver.find_elements(*AboutRentLocators.SCOOTER_COLORS)[color].click()

driver.find_element(*AboutRentLocators.COMMENT_FOR_THE_COURIER).send_keys("При привозите с утра, сплю до 12:00!!")

driver.find_element(*AboutRentLocators.BUTTON_TO_ORDER).click()
driver.find_elements(*AboutRentLocators.MODAL_FORM_BUTTONS)[1].click()
# driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]").click()

time.sleep(3)
print(driver.find_element(*OrderPageLocators.ORDER_STATUS_INFO).text)

print("Заказ оформлен" in driver.find_element(*OrderPageLocators.ORDER_STATUS_INFO).text)


time.sleep(1)
driver.quit()
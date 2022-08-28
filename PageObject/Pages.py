import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


from PageObject.locators import *


class ActionOnPage:
    @staticmethod
    def wait_element(driver, xpath_element):
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"{xpath_element}")))

    @staticmethod
    def accept_cookie(driver):
        driver.find_element(*MainPageLocators.BUTTON_ACCEPT_COOKIES).click()

    @staticmethod
    def scroll_down(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def scroll_up(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollLow);")

    @staticmethod
    def scroll_to_element(driver, xpath_element):
        driver.execute_script("arguments[0].scrollIntoView();", f"{xpath_element}")

    @staticmethod
    def checking_the_current_tab(driver):
        number_of_tabs = len(driver.window_handles)
        if number_of_tabs > 1:
            driver.switch_to.window(driver.window_handles[-1])
            element_tab_yandex = ".//*[@name='text']"
            ActionOnPage().wait_element(driver, element_tab_yandex)


class MainPage:
    @staticmethod
    @allure.step("Кликаем на кнопку меню аккордиона")
    def click_on_question_and_check_answer(driver, question_pos):
        ActionOnPage().scroll_down(driver)
        ActionOnPage().wait_element(driver, MainPageLocators.QUESTIONS_ACCORDION[1])

        button_accordions = driver.find_elements(*MainPageLocators.QUESTIONS_ACCORDION)
        button_accordions[question_pos].click()

        ActionOnPage().wait_element(driver, MainPageLocators.QUESTIONS_ABOUT_IMPORTANT[1])
        ActionOnPage().wait_element(driver, MainPageLocators.ACCORDION_MENU[1])

    @staticmethod
    @allure.step("Кликаем на кнопку логотипа")
    def click_on_logo(driver, xpath_element):
        driver.find_element(By.XPATH, f"{xpath_element}").click()

    @staticmethod
    @allure.step("Кликаем кнопку 'Заказать'")
    def click_order(driver, xpath_element):
        driver.find_element(By.XPATH, f"{xpath_element}").click()


class OrderPage:
    @staticmethod
    @allure.step("Вводим Имя")
    def set_name(driver, name):
        driver.find_element(*OrderPageLocators.FIELD_NAME).clear()
        driver.find_element(*OrderPageLocators.FIELD_NAME).send_keys(name)

    @staticmethod
    @allure.step("Вводим Фамилию")
    def set_last_name(driver, last_name):
        driver.find_element(*OrderPageLocators.FIELD_LAST_NAME).clear()
        driver.find_element(*OrderPageLocators.FIELD_LAST_NAME).send_keys(last_name)

    @staticmethod
    @allure.step("Вводим адрес")
    def set_address(driver, address):
        driver.find_element(*OrderPageLocators.FIELD_ADDRESS_WHERE_TO_TAKE).clear()
        driver.find_element(*OrderPageLocators.FIELD_ADDRESS_WHERE_TO_TAKE).send_keys(address)

    @staticmethod
    @allure.step("Вводим номер телефона")
    def set_phone_number(driver, phone_number):
        driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER).clear()
        driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER).send_keys(phone_number)

    @staticmethod
    @allure.step("Выбираем остановку метро")
    def set_metro_station(driver, station):
        driver.find_element(*OrderPageLocators.BOOTSTRAP).click()
        driver.find_element(*OrderPageLocators.BOOTSTRAP).send_keys(station)
        driver.find_element(*OrderPageLocators.BOOTSTRAP).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    @staticmethod
    @allure.step("Кликаем кнопку продолжить")
    def click_next(driver):
        driver.find_element(*OrderPageLocators.NEXT).click()

    @allure.step("Заполняем форму 'Для кого самокат'")
    def enter_order_data(self, driver, name, last_name, address_to_take, station, phone_number):
        ActionOnPage().wait_element(driver, OrderPageLocators.FIELD_NAME[1])
        ActionOnPage().wait_element(driver, OrderPageLocators.FIELD_LAST_NAME[1])
        ActionOnPage().wait_element(driver, OrderPageLocators.FIELD_ADDRESS_WHERE_TO_TAKE[1])
        ActionOnPage().wait_element(driver, OrderPageLocators.BOOTSTRAP[1])
        ActionOnPage().wait_element(driver, OrderPageLocators.FIELD_PHONE_NUMBER[1])

        self.set_name(driver, name)
        self.set_last_name(driver, last_name)
        self.set_address(driver, address_to_take)
        self.set_metro_station(driver, station)
        self.set_phone_number(driver, phone_number)


class AboutRentPage:
    @staticmethod
    @allure.step("Вводим дату доставки")
    def set_when_to_bring(driver, date):
        """
        date format string "dd.mm.yyyy"
        """
        driver.find_element(*AboutRentLocators.WHEN_TO_BRING).send_keys(date)

    @staticmethod
    @allure.step("Выбираем срок аренды")
    def set_rental_period(driver, index):
        driver.find_element(*AboutRentLocators.DROPDOWN_ARROW).click()
        driver.find_elements(*AboutRentLocators.DROPDOWN_MENU)[index].click()

    @staticmethod
    @allure.step("Выбираем цвет самоката")
    def set_scooter_color(driver, color_index):
        """
        color black = index[0] or grey = index[1]
        """
        driver.find_elements(*AboutRentLocators.SCOOTER_COLORS)[color_index].click()

    @staticmethod
    @allure.step("Заполняем сообщение для курьера")
    def set_comment_for_the_courier(driver, message):
        driver.find_element(*AboutRentLocators.COMMENT_FOR_THE_COURIER).send_keys(message)

    @staticmethod
    @allure.step("Кликаем кнопку 'Заказать'")
    def click_on_button_to_order(driver):
        driver.find_element(*AboutRentLocators.BUTTON_TO_ORDER).click()

    @staticmethod
    @allure.step("На модальной форме кликаем кнопку 'Да'")
    def click_yes_on_modal_menu(driver):
        driver.find_elements(*AboutRentLocators.MODAL_FORM_BUTTONS)[1].click()

    @staticmethod
    @allure.step("Получаем информацию по оформленному заказу")
    def completed_order(driver):
        text = driver.find_element(*OrderPageLocators.ORDER_STATUS_INFO).text
        return text

    @allure.step("Заполняем форму 'Про аренду'")
    def enter_about_rent_date(self, driver, date, index, color, message):
        ActionOnPage().wait_element(driver, AboutRentLocators.COMMENT_FOR_THE_COURIER[1])

        self.set_when_to_bring(driver, date)
        self.set_rental_period(driver, index)
        self.set_scooter_color(driver, color)
        self.set_comment_for_the_courier(driver, message)

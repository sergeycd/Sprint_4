import time
import pytest


from allure_commons.types import AttachmentType


from PageObject.Pages import *
from PageObject.Informations import *


class TestQaScooterPraktikumServices:

    @pytest.mark.menu_accordion
    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    @allure.title("Проверяем данные меню 'Вопросы о важном'")
    def test_click_on_question_and_check_answer(selfs, driver, question_index):
        ActionOnPage().accept_cookie(driver)
        MainPage().click_on_question_and_check_answer(driver, question_index)

        assert driver.find_elements(*MainPageLocators.ANSWER_ACCORDION)[question_index].text \
               == TextInfo.DICT_ACCORDION_BUTTONS[driver.find_elements(*MainPageLocators.QUESTIONS_ACCORDION)[question_index].text], \
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot"+str(time.process_time()),
                          attachment_type=AttachmentType.PNG)

    @pytest.mark.click
    @pytest.mark.parametrize('button_logo, url', [pytest.param(MainPageLocators.LOGO_BUTTON_SCOOTER[1],
                                                               "https://qa-scooter.praktikum-services.ru/",
                                                               marks=pytest.mark.logo_scooter),
                                                  pytest.param(MainPageLocators.LOGO_BUTTON_YANDEX[1],
                                                               "https://yandex.ru/",
                                                               marks=pytest.mark.logo_yandex)])
    @allure.title("Проверяем работу кнопки 'Логотип'")
    def test_click_on_logo(self, driver, button_logo, url):
        MainPage().click_on_logo(driver, button_logo)
        ActionOnPage().checking_the_current_tab(driver)

        assert driver.current_url == url, \
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot"+str(time.process_time()),
                          attachment_type=AttachmentType.PNG)

    @pytest.mark.order
    @pytest.mark.xfail  # in browser Chrome fail
    @pytest.mark.parametrize('enter_button, station, name, last_name, address_to_take, '
                             'phone_number, date, index, color_index, message',
                             [pytest.param(MainPageLocators.HEADER_BUTTON_ORDER[1],
                                           "Преображенская площадь", "Евгений", "Греков",
                                           "Новосибирск, ул Большая 213 кв 7", "89607001111",
                                           "23.10.2022", 1, 0, "Привозите после 12:00"),

                              pytest.param(MainPageLocators.MIDDLE_BUTTON_ORDER[1],
                                           "Сокольники", "Елена", "Кафанова",
                                           "Москва, ул Заречная 13 кв 27", "89997774444",
                                           "11.09.2023", 6, 1, "Привозите после 12:00")])
    @allure.title("Проверяем оформление заказа")
    def test_order(self, driver, enter_button, station, name, last_name,
                   address_to_take, phone_number, date, index, color_index, message):
        ActionOnPage().accept_cookie(driver)
        MainPage().click_order(driver, enter_button)

        OrderPage().enter_order_data(driver,
                                     name=name,
                                     last_name=last_name,
                                     address_to_take=address_to_take,
                                     station=station,
                                     phone_number=phone_number)

        OrderPage().click_next(driver)

        AboutRentPage().enter_about_rent_date(driver,
                                              date=date,
                                              index=index,
                                              color=color_index,
                                              message=message)

        AboutRentPage().click_on_button_to_order(driver)
        AboutRentPage().click_yes_on_modal_menu(driver)

        assert "Заказ оформлен" in AboutRentPage().completed_order(driver), \
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot"+str(time.process_time()),
                          attachment_type=AttachmentType.PNG)

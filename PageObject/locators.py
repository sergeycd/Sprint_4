from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO_BUTTON_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")
    LOGO_BUTTON_YANDEX = (By.XPATH, ".//*[@alt='Yandex']")

    HEADER_BUTTON_ORDER = (By.XPATH, ".//*[@class='Button_Button__ra12g']")
    MIDDLE_BUTTON_ORDER = (By.XPATH, ".//*[contains(@class, 'Button_Middle__1CSJM')]")

    QUESTIONS_ABOUT_IMPORTANT = (By.XPATH, ".//div[text()='Вопросы о важном']")
    ACCORDION_MENU = (By.XPATH, ".//*[@class='accordion']")
    QUESTIONS_ACCORDION = (By.XPATH, ".//*[contains(@id, 'accordion__heading-')]")
    ANSWER_ACCORDION = (By.XPATH, ".//*[contains(@id, 'accordion__panel-')]/p")

    BUTTON_ACCEPT_COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")


class OrderPageLocators:
    FIELD_NAME = (By.XPATH, ".//*[@placeholder='* Имя']")
    FIELD_LAST_NAME = (By.XPATH, ".//*[@placeholder='* Фамилия']")
    FIELD_ADDRESS_WHERE_TO_TAKE = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']")
    FIELD_PHONE_NUMBER = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']")

    BOOTSTRAP = (By.XPATH, ".//*[@placeholder='* Станция метро']")

    NEXT = (By.XPATH, ".//*[text()='Далее']")

    ORDER_STATUS_INFO = (By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ']")


class AboutRentLocators:
    WHEN_TO_BRING = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']")
    SCOOTER_COLORS = (By.XPATH, ".//*[@class='Checkbox_Label__3wxSf']")
    COMMENT_FOR_THE_COURIER = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")

    DROPDOWN_ARROW = (By.XPATH, ".//*[@class='Dropdown-arrow']")
    DROPDOWN_MENU = (By.XPATH, ".//*[@class='Dropdown-menu']/div")

    BUTTON_TO_ORDER = (By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') "
                                 "and text()='Заказать']")
    MODAL_FORM_BUTTONS = (By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') "
                                    "and text()='Нет'or text()='Да']")

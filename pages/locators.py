from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>.btn.btn-default")


class BasketPageLocators:
    PRODUCT_LINK_IN_BASKET = (By.CSS_SELECTOR, ".basket-items>.row")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div #content_inner>p")


class LoginPageLocators:
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON_LINK = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    BOOK_NAME_LINK = (By.CSS_SELECTOR, "div .col-sm-6.product_main h1")
    BOOK_NAME_LINK_IN_BASKET = (By.CSS_SELECTOR, "div .alertinner strong")
    BOOK_PRICE_LINK = (By.CSS_SELECTOR, "p.price_color")
    BOOK_PRICE_LINK_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in>.alertinner")




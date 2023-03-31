from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket_link(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        link.click()

    def product_name_must_be_added_to_basket(self):
        name_before = self.browser.find_element(*ProductPageLocators.BOOK_NAME_LINK)
        name_after = self.browser.find_element(*ProductPageLocators.BOOK_NAME_LINK_IN_BASKET)
        assert name_before.text == name_after.text, "Product name in basket doesn't match with original product name"

    def product_price_must_be_added_to_basket(self):
        price_before = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_LINK)
        price_after = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_LINK_IN_BASKET)
        assert price_before.text == price_after.text, "Product price in basket doesn't match with original product " \
                                                      "price "

    def should_not_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "After adding product to basket, success message is presented, but should not be"

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_message_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear after adding product to basket"




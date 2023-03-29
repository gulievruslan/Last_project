from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def go_to_product_page(self):
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

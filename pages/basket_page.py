from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def test_guest_should_see_empty_basket(self):
        assert self.is_not_element_present(*MainPageLocators.PRODUCT_LINK_IN_BASKET), "Basket is not empty, but " \
                                                                                      "should be "
        basket_is_empty_message = self.browser.find_element(*MainPageLocators.BASKET_IS_EMPTY)
        assert "Your basket is empty" in basket_is_empty_message.text, "Basket is empty message not presented, but " \
                                                                       "should be "

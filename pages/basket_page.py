from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def test_guest_should_see_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LINK_IN_BASKET), "Basket is not empty, but " \
                                                                                      "should be "

    def test_quest_should_see_basket_is_empty_message(self):
        basket_is_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert "Your basket is empty" in basket_is_empty_message.text, "Basket is empty message not presented, but " \
                                                                       "should be "

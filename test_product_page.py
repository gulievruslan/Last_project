import time

from .pages.product_page import ProductPage
import pytest

promo_num = [pytest.param(i, marks=pytest.mark.xfail(reason='some bug')) if i == 7 else i for i in range(10)]


@pytest.mark.skip
@pytest.mark.parametrize('link', promo_num)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_link()
    page.solve_quiz_and_get_code()
    page.product_name_must_be_added_to_basket()
    page.product_price_must_be_added_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_link()
    page.should_not_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_see_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_link()
    page.should_disappear_message_after_adding_product_to_basket()

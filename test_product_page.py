from .pages.product_page import ProductPage
import pytest

promo_num = [pytest.param(i, marks=pytest.mark.xfail(reason='some bug')) if i == 7 else i for i in range(10)]


@pytest.mark.parametrize('link', promo_num)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.product_name_must_be_added_to_basket()
    page.product_price_must_be_added_to_basket()
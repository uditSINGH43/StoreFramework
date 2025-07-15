#pytest -m smoke // Tagging
#pytest -n 10 // pytest-xdist plugin you need to run in parallel
 #pytest -n 3 pytest_e2eframework.py -m smoke --browser_name Edge --html=reports/report.html

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json

import pytest

from pageObjects.login import LoginPage

test_data_path = 'C:/Users/Udit Singh/PycharmProjects/Pythontest/data/test_e2eFramework.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    Checkout_Confirmation = shop_page.cart()
    Checkout_Confirmation.checkout()
    Checkout_Confirmation.enter_delivery("ind")
    Checkout_Confirmation.confirm()

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    BSortedVeggie = []
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # click on column header
    driver.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()

    # collect all veggie names -> BrowserSort (A,B,C)
    BrowserSort = driver.find_elements(By.XPATH, "//tr/td[1]")
    for element in BrowserSort:
        BSortedVeggie.append(element.text)

    originalBrowserSort = BSortedVeggie.copy()

    # Sort the BrowserSort -> newSort (A,B,C)
    BSortedVeggie.sort()
    assert BSortedVeggie == originalBrowserSort

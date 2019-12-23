import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    chrome_options = Options()
    chrome_options.headless = True
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('file://./code/app/calculator.html')
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

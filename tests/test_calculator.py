import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.mark.parametrize(
    'count, price, state_code_index, expected_result', [
    (100, 10, 5, 1082.5),
    (1000, 10, 1, 10364.45),
    (5000, 10, 2, 51300),
    (7000, 10, 3, 69168.75),
    (10000, 10, 4, 93600),
    (50000, 10, 5, 460062.5),
    ])
def test_calculate(
        driver,count, price,  state_code_index, expected_result):
    driver.refresh()
    driver.find_element_by_id('count').send_keys(count)
    
    select = Select(driver.find_element_by_id('state_code'))
    select.select_by_index(state_code_index)
    
    driver.find_element_by_id('price').send_keys(price)
    assert (driver.find_element_by_id('result').get_attribute('value') ==
        str(expected_result))


@pytest.mark.parametrize(
    'count, discount', [
    (1, None),
    (999, None),
    (1000, '1000'),
    (4999, '1000'),
    (5000, '5000'),
    (6999, '5000'),
    (7000, '7000'),
    (9999, '7000'),
    (10000, '10000'),
    (49999, '10000'),
    (50000, '50000'),
    (999999, '50000'),
    ])
def test_discount_display(driver, count, discount):
    driver.refresh()
    driver.find_element_by_id('count').send_keys(count)
    target_id = f'discount_{discount}'
    for li in driver.find_elements_by_class_name('list-group-item'):
        if li.get_attribute('id') == target_id:
            assert 'list-group-item-primary' in li.get_attribute('class')
        else:
            assert 'list-group-item-primary' not in li.get_attribute('class')


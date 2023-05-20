import random
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy


def test_home(app_run) -> None:
    el_phone = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/etPhone")
    el_name = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/etUsername")
    el_age = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/etAge")
    el_btn_login = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/btNext")
    el_gender = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/rbMale")
    assert el_phone is not None
    assert el_name is not None
    assert el_gender is not None
    assert el_age is not None
    assert el_btn_login is not None
    el_gender.click()
    el_phone.send_keys("13040811560")
    el_name.send_keys("xpf")
    el_age.send_keys("13")
    el_btn_login.click()


def test_options(app_run, rand_num=random.randint(0, 15)):
    # 生成 4 位二进制随机数
    # 生成一个随机数，范围为 0 到 15
    el_pressure = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/cbBloodPressure")
    el_uric = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/cbUricAcid")
    el_oxygen = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/cbBloodOxygen")
    el_sugar = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/cbBloodSugarLevel")
    for index in range(4):
        index_cancel = rand_num & (1 << index) == 0
        target_el = None
        if index == 0:
            target_el = el_pressure
        elif index == 1:
            target_el = el_uric
        elif index == 2:
            target_el = el_oxygen
        elif index == 3:
            target_el = el_sugar
        print(target_el.get_dom_attribute("checked"))
        assert target_el is not None
        assert target_el.get_dom_attribute("checked") == "true"
        if index_cancel:
            target_el.click()


def test_confirm(app_run, confirm=True):
    el_next = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/btNext")
    el_next.click()
    el_ok = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/btConfirm")
    el_cancel = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/btCancel")
    assert el_next is not None
    assert el_ok is not None
    assert el_cancel is not None
    if confirm:
        el_ok.click()
    else:
        el_cancel.click()


def test_pay(app_run):
    el_next = app_run.find_element(by=AppiumBy.ID, value="sinocare.multicriteriasdkdemo:id/btNext")
    assert el_next is not None


def test_test(app_run):
    time.sleep(5)
    el_perm_allow = app_run.find_element(by=AppiumBy.ID,
                                         value="com.android.permissioncontroller:id/permission_allow_button")
    el_perm_deny = app_run.find_element(by=AppiumBy.ID,
                                        value="com.android.permissioncontroller:id/permission_deny_button")
    assert el_perm_allow is not None
    assert el_perm_deny is not None
    el_perm_allow.click()
    # el_perm_deny.click()


def test_steps(app_run):
    el_prev = app_run.find_element(by=AppiumBy.ID,
                                   value="sinocare.multicriteriasdkdemo:id/btPrevious")
    el_next = app_run.find_element(by=AppiumBy.ID,
                                   value="sinocare.multicriteriasdkdemo:id/btNext")
    assert el_prev is not None
    assert el_next is not None
    while el_next.get_dom_attribute("enabled") == "true":
        el_next.click()
    while el_prev.get_dom_attribute("enabled") == "true":
        el_prev.click()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    pytest.main(['-s', 'test_pytest.py'])

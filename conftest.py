import subprocess
import time

import pytest
from appium import webdriver
import os

appPath = r"E:\github\HealthcareDetectionAndroid\app\build\outputs\apk\debug"
appName = "cegao-1.0-2023-05-21-03-53-49.apk"

for f in os.listdir(appPath):
    if f.endswith("apk"):
        appName = f

emulatorName = "emulator-5554"
capabilities = {
    "platformName": "Android",

    "appium:options": {
        "automationName": 'UiAutomator2',
        "deviceName": emulatorName,
        "platformVersion": "12",
        "app": rf"{appPath}\{appName}",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "language": 'en',
        "locale": 'US'
    }
}

appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope='session')
def app_run(request):
    subprocess.Popen(r"appium", shell=True)
    launched = False
    # 等待模拟器启动
    while True:
        try:
            # 使用 adb 命令查询模拟器状态
            result = subprocess.check_output("adb devices")
            if emulatorName in result.decode():
                print("模拟器已启动")
                break
            elif not launched:
                subprocess.Popen(fr"D:\Android\Sdk\emulator\emulator.exe -avd 17API31", shell=True)
                launched = True
        except subprocess.CalledProcessError:
            pass
        time.sleep(2)
    # subprocess.Popen(r"D:\Android\Sdk\emulator\emulator.exe -avd 17API31", shell=True)
    driver = webdriver.Remote(appium_server_url, capabilities)
    driver.reset()

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)
    return driver

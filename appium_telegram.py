
import random
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import subprocess

ADB = 'C:\\Users\\User\\AppData\\Local\\Android\\Sdk\\platform-tools'

desired_caps = {}
desired_caps["unicodeKeyboard"] = True
desired_caps['fullReset'] = False
desired_caps['noReset'] = True
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['automationName'] = 'Appium'
desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['app'] = 'C:/Users/User/Desktop/Alex/Telegram Android.apk'
desired_caps["appPackage"] = "org.telegram.messenger"
desired_caps["appActivity"] = "org.telegram.ui.LaunchActivity"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
index = 0


def cancel_popup():
    for _ in range(2):
        try:
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("CANCEL")').click()
        except:
            pass
cancel_popup()

def delete_contact():
    user_action.tap(x=1000, y=134).perform()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("Delete contact")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("OK")').click()
    sleep(2)
    subprocess.call("adb -s emulator-5554 shell am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity -S",shell=True, cwd='C:\\Users\\User\\AppData\\Local\\Android\\Sdk\\platform-tools')
    sleep(1)


def input_text_messege():
    messedge = driver.find_element_by_class_name("android.widget.EditText")
    string_sub = ["Подписывайтесь", "Переходите", "Заходите", "Подписывайся"]
    string_fun = ["ПРИЗЫ ","ПРИЗЫ за ПОДПИСКУ ","АКЦИЯ НА КАНАЛЕ ","БЛАГОДАРНОСТЬ ПОДПИСЧИКАМ "]
    messedge.send_keys(random.choice(string_fun)," https://www.youtube.com/channel/UCWH8XQ_zwv0ijB4glJFOm8A  ", random.choice(string_sub), ' на каналы новые полезные видео присоединяйтесь!! ')
    sleep(3)
    user_action.tap(x=1000, y=1734).perform()
    sleep(3)
    messedge1 = driver.find_elements_by_class_name("android.view.View")
    messedge1[0].click()


for i in range(45):
    sleep(4)
    user_action = TouchAction(driver)
    user_action.tap(x=950, y=1680).perform()
    sleep(4)
    dd = driver.find_elements_by_class_name("android.widget.FrameLayout")
    dd[0].click()
    sleep(3)
    input_text_messege()
    # sleep(3)
    # messedge1[1].click()
    sleep(3)
    delete_contact()

    index+=1
    print(index)



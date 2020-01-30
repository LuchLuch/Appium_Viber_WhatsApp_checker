import sqlite3
import subprocess
from threading import Thread
import time

start_time = time.time()
adb = 'C:\\Users\\ac86\\AppData\\Local\\Android\\Sdk\\platform-tools'


def run_em(dev):
    adb1 = 'C:\\Users\\ac86\\AppData\\Local\\Android\\Sdk\\emulator'
    strr = ("emulator " + dev + " -noaudio")
    try:
        subprocess.call(strr, shell=True, cwd=adb1, timeout=2)
    except:
        print("Done")


def clear_contacts_list():
    time.sleep(5)
    subprocess.check_call("adb kill-server", shell=True, cwd=adb)
    subprocess.check_call("adb start-server", shell=True, cwd=adb)
    print("Очистка старых контактов")
    subprocess.call("adb shell pm clear com.android.providers.contacts", shell=True, cwd=adb)  # clear contacts
    time.sleep(15)


def create_and_push_contacts():
    c = open("00006.vcf", "w")
    f1 = open("HOMEPA_HA_nPOBEPKy.txt", "r")
    for_check = []  # all from number_for_viber
    LEN_NUMB = 0
    for i in f1:
        LEN_NUMB += 1
        i = i.rstrip()
        for_check.append(i)
        done = ("BEGIN:VCARD\nVERSION:2.1\nN:;%s;;;\nFN:%s\nTEL;CELL:+%s\nEND:VCARD\n") % (i, i, i)
        c.write(done)
    f1.close()
    c.close()
    "загрузка контактов через adb"
    subprocess.call("adb push C:\\Users\\ac86\\PycharmProjects\\untitled\\CHECKER_Viber_WhatsApp\\00006.vcf /storage/sdcard",shell=True, cwd=adb)  # push contacts to phone
    time.sleep(21)
    subprocess.call("adb shell am start -t 'text/vcard' -d 'file:///sdcard/00006.vcf' -a android.intent.action.VIEW com.android.contacts",shell=True, cwd=adb)  # add contacts to contacts list
    print("Загрузка новых контактов")
    time.sleep(21)
    subprocess.call("adb shell am start -n com.android.contacts/com.android.contacts.common.list.CustomContactListFilterActivity -S",shell=True, cwd=adb)
    time.sleep(21)


def whatsapp_refreshe_contacts():
    # user_action = TouchAction(driver)
    subprocess.call("adb shell am start -n com.whatsapp/com.whatsapp.ContactPicker", shell=True, cwd=adb)
    time.sleep(4)
    subprocess.call("adb shell input tap 1000 150", shell=True, cwd=adb)
    # user_action.tap(x=1000, y=150).perform()
    time.sleep(4)
    subprocess.call("adb shell input tap 700 400", shell=True, cwd=adb)
    # user_action.tap(x=700, y=400).perform()
    time.sleep(4)
    subprocess.call("adb shell am start -n com.viber.voip/com.viber.voip.contacts.ui.ContactsComposeListActivity -S", shell=True, cwd=adb)
    time.sleep(3)


def parse_whatsapp():
    time.sleep(211)  # fgerftgertertertert
    insertt = open("3A6PATb_HOMEPA.txt", "w")
    insertt.write("")
    insertt = open("3A6PATb_HOMEPA.txt", "a")
    subprocess.check_call("adb pull /data/data/com.android.providers.contacts/databases/contacts2.db C:\\Users\\ac86\\PycharmProjects\\untitled\\CHECKER_Viber_WhatsApp",shell=True, cwd=adb)
    time.sleep(8)
    conn = sqlite3.connect("C:\\Users\\ac86\\PycharmProjects\\untitled\\CHECKER_Viber_WhatsApp\\contacts2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT data1 FROM data WHERE data2 = 'WhatsApp'")
    results = cursor.fetchall()
    results = set(results)
    print(len(results))
    insertt.write('\n' + 'WhatsApp ' '\n')
    for i in results:
        whatsapp = i[0].split("@")
        c = str(whatsapp[0]) + "\n"
        insertt.write(c)
    insertt.close()


def parse_viber():
    insertt = open("3A6PATb_HOMEPA.txt", "a")
    adb = 'C:\\Users\\ac86\\AppData\\Local\\Android\\Sdk\\platform-tools'
    subprocess.check_call("adb pull /data/data/com.android.providers.contacts/databases/contacts2.db C:\\Users\\ac86\\PycharmProjects\\untitled\\CHECKER_Viber_WhatsApp",shell=True, cwd=adb)
    time.sleep(2)
    conn = sqlite3.connect("C:\\Users\\ac86\\PycharmProjects\\untitled\\CHECKER_Viber_WhatsApp\\contacts2.db")
    cursor = conn.cursor()
    # cursor.execute("SELECT data1 FROM data WHERE data3 LIKE '%Бесплатное%'")
    cursor.execute("SELECT data1 FROM data WHERE data3 LIKE '%Free%'")
    # Получаем результат сделанного запроса
    set_viber_contacts = set(cursor.fetchall())
    print(len(set_viber_contacts))
    insertt.write('Viber '* 3 + '\n\n')
    for i in set_viber_contacts:
        i = str(i[0].strip("+")) + "\n"
        insertt.write(i)

    insertt.close()
    end_time = time.time()
    print((end_time - start_time) / 60)
    print("ВСЁ ПРОВЕРЕНО")
    if len(set_viber_contacts)==0:
        reopen_devices()
    else:
        adb = 'C:\\Users\\ac86\\AppData\\Local\\Android\\Sdk\\platform-tools'
        subprocess.check_call("adb -s emulator-5554 emu kill", shell=True, cwd=adb)


def reopen_devices():
        print("viber 0")
        subprocess.check_call("adb -s emulator-5554 emu kill", shell=True, cwd=adb)
        time.sleep(12)
        run_em("@reserve_WhatsApp_Viber")
        clear_contacts_list()
        create_and_push_contacts()
        whatsapp_refreshe_contacts()
        parse_whatsapp()
        parse_viber()



run_em("@WhatsApp_Viber")
clear_contacts_list()
create_and_push_contacts()
whatsapp_refreshe_contacts()
parse_whatsapp()
parse_viber()


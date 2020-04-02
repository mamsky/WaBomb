from selenium import webdriver
import sys
import psutil
import getpass 
import os
def banner():
        print('\033[94m==========================================')
        print('''\033[91m==========================================|
| ______  ___  ______ _______   __    |   |
| | ___ \/ _ \ | ___ \  _  \ \ / /    |   |
| | |_/ / /_\ \| |_/ / | | |\ V /     |   |
| |  __/|  _  ||  __/| | | | \ /      |   |
| | |   | | | || |   \ \_/ / | |      |   |
| \_|   \_| |_/\_|    \___/  \_/      |   |
|                                     |   |
|buatan sansboy by: Paste             |   |
==========================================|''')
        print('\033[94m==========================================')
banner()
def main():
        driver = webdriver.Chrome()
        driver.get("https://web.whatsapp.com/")
        name = raw_input('\033[93m Name: ')
        msg = raw_input('\033[95m Kata Bijakmu Pantek: ')
        count = int(raw_input('\033[94m Berapa Banyak Tot: '))

        print ('')
        print ('Tunggu bentar cok')
        print ('Sabar Napa')

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        # The classname of message box may vary.
        msg_box = driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="1"][@spellcheck="true"]')
        for i in range(0, count):
                print('\033[1;4m[=] ',i+1, "Asikkk Berhasil Cok!!!! :", name)
                msg_box.send_keys(msg)
                # The classname of send button may vary.
                button = driver.find_element_by_xpath('//button[@class = "_35EW6"]')
                button.click() 
        print('Meledak Cok!!')

main()

import random
import pyfiglet
import webbrowser
import os
from colorama import Fore
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


driver = None  # Global variable to store the driver object


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://web.whatsapp.com/')
    return driver


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    colors = [Fore.MAGENTA, Fore.WHITE, Fore.MAGENTA, Fore.MAGENTA, Fore.WHITE, Fore.MAGENTA]
    figlet = pyfiglet.Figlet(font="stop")
    banner_text = figlet.renderText('WB0MB')

    for idx, line in enumerate(banner_text.split('\n')):
        print(f"{colors[idx % len(colors)]}{line}")
        sleep(0.05)

    print(Fore.RESET)


def send_messages():
    name = input('Enter the name of user or group: ')
    message = input('Enter your message: ')
    try:
        count = int(input('Enter the count: '))
    except ValueError:
        print("❌ Invalid number. Please enter an integer.")
        return

    input("Press Enter once you have scanned the QR code and are ready.")

    try:
        user = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@title='{name}']"))
        )
        user.click()
        print(f"✅ Found and opened chat with '{name}'")
    except TimeoutException:
        print("❌ Failed to find the contact or group. Make sure the name is correct and visible in your WhatsApp list.")
        return

    sleep(2)

    try:
        msg_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//footer//div[@contenteditable='true'][@data-tab]"))
        )
        print("✅ Message box located.")
    except Exception as e:
        print(f"❌ Failed to locate the message input box: {e}")
        return

    try:
        for i in range(count):
            msg_box.send_keys(message)
            msg_box.send_keys(Keys.ENTER)
            sleep(0.1)
        print("✅ Bombing Complete!!")
    except Exception as e:
        print(f"❌ Error during message sending: {e}")

    sleep(2)


def menu():
    clear_screen()
    show_banner()

    while True:
        print("""
        1. Start bombing
        2. Support original creator
        3. Exit/Quit
        """)

        choice = input("What would you like to do? ")

        if choice == "1":
            clear_screen()
            send_messages()
        elif choice == "2":
            webbrowser.open('https://github.com/mamosdev/Bombers/')
            print("\nThanks for supporting the original creator!")
            sleep(1)
        elif choice == "3":
            print("\nGoodbye")
            break
        else:
            print("\n❌ Not a valid choice. Try again.")
            sleep(1)


if __name__ == "__main__":
    driver = setup_driver()
    input("Scan the QR code in the browser and press Enter when ready...")
    menu()

from time import sleep
from Variables.configs import *
from Variables.elements import *
from appium import webdriver


class Keywords:
    def __init__(self):
        self.driver_instance = None

    def open_whatsapp(self, udid=None):
        udid = udid or device_udid
        # path = join(str(self.get_project_root()), 'whatsapp', 'App', 'whatsapp.apk')
        caps = {
            'app': app_apk,'platformName': device_platform, 'deviceName': device_name, 'automationName': 'UiAutomator2',
            'skipServerInstallation': True, 'appActivity': app_activity, 'noReset': no_reset,
            'udid': udid, 'newCommandTimeout': 1200, 'autoGrantPermissions': True,
            'appPackage': app_package, 'systemPort': int(float(system_port)),
            'disableWindowAnimation': False
        }
        driver = webdriver.Remote(str(appium_server), caps)
        self.driver_instance = driver
        return driver

    def find(self, locator, el_type='id', timeout=1):
        el_type = el_type.lower()
        driver = self.driver_instance
        for try_number in range(int(timeout/0.5)):
            try:
                if el_type == 'xpath':
                    return driver.find_element_by_xpath(locator)
                elif el_type == 'id':
                    return driver.find_element_by_id(locator)
            except:
                sleep(0.5)
        raise Exception(f'Cannot find the element {str(locator)}')

    def get_contacts_list(self):
        with open('../contacts.vcf', mode='r') as vcf:
            contacts = []
            for line in vcf:
                if "FN:" in line:
                    line = line.replace("FN:", '').replace("\n", '')
                    contacts.append(line)
                    contacts.sort()
            print(contacts)
            return contacts

    def click_on_search(self):
        self.find(search_button, timeout=2).click()
        self.find(search_input, timeout=2)

    def set_text_to_contact_search(self, text):
        self.find(search_input, timeout=2).set_text(text)

    def click_on_contact_from_contact_search(self, contact):
        self.find(contacts_search_result, timeout=2)
        text = self.find(contacts_search_result).text
        if text == contact:
            self.find(contacts_search_result, timeout=2).click()
        else:
            raise Exception(f'Cannot find {contact} in search')

    def set_message_body(self, message):
        self.find(message_entry, timeout=2).set_text(message)

    def click_on_send_button(self):
        self.find(send_button, timeout=2).click()

    def click_on_back_button(self):
        self.find(back_button, timeout=2).click()

    def click_on_new_message_button(self):
        self.find(send_new_message_button, timeout=2).click()

    def check_app_in_main(self):
        activity = self.driver_instance.current_activity
        assert activity == home_activity
        # self.find_text("WhatsApp")

    def send_message_to_contact(self, contact_name, message_body):
        self.check_app_in_main()
        self.click_on_new_message_button()
        self.click_on_search()
        self.set_text_to_contact_search(contact_name)
        try:
            self.click_on_contact_from_contact_search(contact_name)
        except:
            self.click_on_back_button()
            self.click_on_back_button()
            return False
        self.set_message_body(message_body)
        self.click_on_send_button()
        self.click_on_back_button()
        return True

    def send_bulk_message(self, message):
        counter = 0
        list = self.get_contacts_list()
        for i in list:
            action = self.send_message_to_contact(contact_name=i, message_body=message)
            if not action:
                counter = counter + 1
                print("{} contacts not found ".format(counter))
            else:
                print("Sent to: {}".format(i))

    def teardown(self):
        self.driver_instance.quit()

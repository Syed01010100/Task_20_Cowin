from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CowinURL:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def start(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"Error while accessing the URL: {e}")
            return False

    def click_FAQ_Partners(self):

        if self.start():
            wait = WebDriverWait(self.driver, 10)
            try:
                # Click on the FAQ link
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a'))).click()
                # Click on the Partners link
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a'))).click()
            except Exception as e:
                print(f"Error while creating windows: {e}")

    def fetch_window_ids(self):
        window_handles = self.driver.window_handles
        for handle in window_handles:
            print(f"Window ID: {handle}")

    def close(self):
        window_handles = self.driver.window_handles

        if len(window_handles) > 1:
            try:
                self.driver.switch_to.window(window_handles[1])
                self.driver.close()

                self.driver.switch_to.window(window_handles[1])
                self.driver.close()

                self.driver.switch_to.window(window_handles[0])
            except Exception as e:
                print(f"Error while closing windows: {e}")
        self.driver.quit()


"""if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    cowin_instance = CowinURL(url)
    cowin_instance.create_faq_and_partner_windows()
    cowin_instance.fetch_window_ids()
    cowin_instance.close_windows()"""
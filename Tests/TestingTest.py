import time

from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage
from Tests.BasePage import BasePage


class SearchTest(BasePage):

    def test_search_page(self):
        loginPage = LoginPage(self.driver)
        time.sleep(10)
        text = loginPage.copy_the_text()
        print(text)
        loginPage.send_text(text)
        loginPage.click_verify()

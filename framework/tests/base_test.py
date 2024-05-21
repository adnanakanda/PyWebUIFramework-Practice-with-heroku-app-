import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile

from framework.forms.main_form import MainForm
from framework.utils.browser_factory import BrowserFactory


class Test_base:
    __main_form: MainForm = MainForm()

    @pytest.fixture(scope="session", autouse=True)
    def prepare_browser_factory(request):
        PyQualityServices.browser_factory = BrowserFactory()
        settings = JsonSettingsFile("config.json")
        #self.test_data = JsonSettingsFile("test_data.json")

        browser = PyQualityServices.get_browser()
        browser.maximize()
        browser.go_to(settings.get_value("url"))

        yield

        browser.quit()

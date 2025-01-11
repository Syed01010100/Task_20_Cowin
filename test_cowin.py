# test_cowin.py

import pytest
from cowin import CowinURL

@pytest.fixture(scope="module")
def setup():

    url = "https://www.cowin.gov.in/"
    cowin_instance = CowinURL(url)
    yield cowin_instance
    cowin_instance.driver.quit()

def test_start(setup):

    assert setup.start() is True

def test_click_FAQ_Partner_window(setup):

    setup.click_FAQ_Partners()
    window_handles = setup.driver.window_handles
    assert len(window_handles) > 1

def test_fetch_id(setup):

    setup.click_FAQ_Partners()
    window_handles = setup.driver.window_handles
    IDs = [handle for handle in window_handles]
    print("Opened Window IDs:", IDs)
    assert len(IDs) >= 1

if __name__ == "__main__":
    pytest.main()
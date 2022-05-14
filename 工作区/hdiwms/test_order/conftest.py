import datetime
import time
import requests
import json
import decimal
import pytest
import allure
import copy


@pytest.fixture(scope="session")
def fixorder():
    today = datetime.date.today()
    da1 = datetime.datetime.strftime(today, "%Y%m%d")
    now = time.strftime("%H%M%S")
    da2 = 'S' + da1 + now
    return da2
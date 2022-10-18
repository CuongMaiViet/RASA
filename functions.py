import json
import datetime
import string
import requests
import re


def cap(str):
    return str.capitalize()


def capAll(str):
    return string.capwords(str)


def read_json(file):
    with open(f'{file}', "r", encoding='utf-8') as db:
        data = json.load(db)
    return data


def write_json(file, obj):
    with open(f'{file}', "w", encoding='utf-8') as db:
        json.dump(obj, db)
    return


def get_current_period():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        return "sáng"
    elif 12 <= currentTime.hour < 18:
        return "chiều"
    else:
        return "tối"


def check_agent_availability(url, token):
    headers = {"api_access_token": token}

    r = requests.get(url=url, headers=headers)
    if not r.ok:
        return "Failed to check"

    data = r.json()
    return any(val["availability_status"] == "online" for val in data)


def check_name(name):
    capitalized_name = capAll(name)
    data = read_json("name.json")
    # next((val for val in data if capitalized_name in val['full_name']), None)
    return next((val for val in data if capitalized_name in val['first_name']), None)


def is_valid_email(email):
    if not isinstance(email, str):
        print("email is not string")
        return

    API_KEY = "d60b69d60e5c48e2a69db1d955226dea"
    URL = f"https://emailvalidation.abstractapi.com/v1/?api_key={API_KEY}&&email={email}"
    r = requests.get(url=URL)
    if not r.ok:
        return "Failed to check"

    data = r.json()
    return data.get("deliverability")


def is_valid_phone_number(input):
    API_KEY = "b5eed873d72d4459ae31771225a5bd0c"
    phone = ""

    if not isinstance(input, str):
        print("Phone is not string")
        return

    if input.startswith("0"):
        phone = input.replace("0", "84")
    elif input.startswith("84") or input.startswith("+84"):
        phone = input

    URL = f"https://phonevalidation.abstractapi.com/v1/?api_key={API_KEY}&phone={phone}"
    r = requests.get(url=URL)

    data = r.json()
    return data


def is_valid_site(url):
    if not isinstance(url, str):
        print("url is not string")
        return

    URL = "https://api.geekflare.com/up"
    HEADER = {"x-api-key": "54c7cbb9-209c-464f-8cf1-62b8728d10f9"}
    BODY = {"url": url, "followRedirect": True, "proxyCountry": "vi"}

    r = requests.post(url=URL, headers=HEADER, json=BODY)
    data = r.json()
    return data.get("message")


def is_alphabet(str):
    if str.replace(" ", "").isalpha():
        return True
    else:
        return False


print(check_name("Nam"))



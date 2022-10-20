import json
import datetime
import string
import requests


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

    r = requests.get(url=f"{url}/agents", headers=headers)
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

    ABSTRACT_API_KEY = "d60b69d60e5c48e2a69db1d955226dea"
    ABSTRACT_API = f"https://emailvalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&&email={email}"
    r = requests.get(url=ABSTRACT_API)
    if r.status_code == 422:
        NEUTRINO_USER_ID = "l9931451"
        NEUTRINO_API_KEY = "s8NYkqxQqmJHlJFQX3EE3Lz8dFRgxjkFDFgGQnrAYiQnbedP"
        NEUTRINO_API = "https://neutrinoapi.net/email-verify"
        r = requests.post(url=NEUTRINO_API, json={
                          "user-id": NEUTRINO_USER_ID, "api-key": NEUTRINO_API_KEY, "email": email})
    if r.status_code == 400:
        REACHER_API_KEY = "27c923de-5050-11ed-bedf-f73f2d8f00b6"
        REACHER_API = "https://api.reacher.email/v0/check_email"
        r = requests.post(url=REACHER_API, headers={
                          "authorization": REACHER_API_KEY}, json={"to_email": email})
    if not r.ok:
        EMAILABLE_API_KEY = "live_de390a30809439e05847"
        EMAILABLE_API = f"https://api.emailable.com/v1/verify?email={email}&api_key={EMAILABLE_API_KEY}"
        r = requests.get(url=EMAILABLE_API)
        
    data = r.json()
    if data.get("deliverability") != None:
        return data.get("deliverability") == "DELIVERABLE"
    elif data.get("verified") != None:
        return data.get("verified")
    elif data.get("smtp").get("is_deliverable") != None:
        return data.get("smtp").get("is_deliverable")
    elif data.get("state") != None:
        return data.get("state") == "deliverable"


def is_valid_phone_number(input):
    API_KEY = "b5eed873d72d4459ae31771225a5bd0c"
    phone = ""

    if not isinstance(input, str):
        print("Phone is not string")
        return

    if input.startswith("0"):
        phone = f"84{input[1:]}"
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


def search_eTouch_contact(search_string, url, token, include_contact_inboxes=False):
    headers = {"api_access_token": token}
    r = requests.get(
        url=f"{url}/contacts/search?include_contact_inboxes={include_contact_inboxes}&&q={search_string}",
        headers=headers
    )
    data = r.json()
    if data.get("payload") == []:
        return None
    return data


print(is_valid_email("abc@gmail.com"))

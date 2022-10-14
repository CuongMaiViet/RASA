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
    return next((val for val in data if capitalized_name in val['full_name']), None)

def is_valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


def is_valid_e164(phone):
    regex = r'^\+[1-9]\d{9,10}$'
    if(re.fullmatch(regex, phone)):
        return True
    else:
        return False


def is_valid_domain(phone):
    regex = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]'
    if(re.fullmatch(regex, phone)):
        return True
    else:
        return False


def is_alphabet(str):
    if str.replace(" ", "").isalpha():
        return True
    else:
        return False


# print(check_name('Hồ Cường'))

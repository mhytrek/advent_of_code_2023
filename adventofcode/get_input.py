import requests
import warnings

#Here paste your data
COOKIES_VALUE = ""
USER_AGENT = ""

def download_input(day:int):
    global COOKIES_VALUE
    global USER_AGENT
    url = f"https://adventofcode.com/2023/day/{day}/input"
    r = requests.get(url, cookies={'session': COOKIES_VALUE}, headers={'User-Agent': USER_AGENT})

    open(f"input_day_{day}", 'wb').write(r.content)
    file = open(f"input_day_{day}")
    lines = file.readlines()
    return lines

print(download_input(1))
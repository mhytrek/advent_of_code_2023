import requests
from bs4 import BeautifulSoup

#Here paste your data
COOKIES_VALUE = ""
USER_AGENT = ""

def download_input(day:int):
    global COOKIES_VALUE
    global USER_AGENT
    url = f"https://adventofcode.com/2023/{day}/input"
    r = requests.get(url, cookies={'session': COOKIES_VALUE}, headers={'User-Agent': USER_AGENT})
    open(f"input_day_{day}", 'wb').write(r.content)

def get_input(day:int):
    try:
        file = open(f"input_day_{day}")
    except FileNotFoundError:
        download_input(day)
        file = open(f"input_day_{day}")
    lines = file.readlines()
    return lines

def get_soup(day:int):
    global COOKIES_VALUE
    global USER_AGENT
    url = f"https://adventofcode.com/2023/day/{day}"
    page = requests.get(url, cookies={'session': COOKIES_VALUE}, headers={'User-Agent': USER_AGENT})
    soup = BeautifulSoup(page.text, 'html')
    return soup

def get_example(day:int):
    soup = get_soup(day)
    soup.find_all("<p>For example</p>")
    code = soup.find_all("code")
    return str(code[0])[len("<code>"):-len("</code>")]

def check_example(day:int, task:int, answer:int):
    soup = get_soup(day)
    if task != 2 and task != 1:
        print("Wrong task number")
        return
    elif task == 2:
        part2 = soup.find_all('article')[1]
        code = part2.find_all("code")
        result = str(code[-1])[len("<code>" + "<em>"):-len("</em>"+"</code>")]
    else:
        part1 = soup.find_all('article')[0]
        code = soup.find_all("code")
        result = str(code[-1])[len("<code>" + "<em>"):-len("</em>" + "</code>")]
    if result == str(answer):
        return "It is working!!"
    else:
        return "Try again"


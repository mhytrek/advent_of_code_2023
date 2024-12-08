import requests
from bs4 import BeautifulSoup

#Here paste your data
COOKIES_VALUE = "53616c7465645f5ff8113e1b13fd3e54401b3847dab1da83b494b80ae38f8715ed322ca00f78d92b06ec94902f92e5020cb130e349270a1bcfe3c262beb69320"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"
YEAR = 2024

def download_input(day:int):
    global COOKIES_VALUE
    global USER_AGENT
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
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
    url = f"https://adventofcode.com/{YEAR}/day/{day}"
    page = requests.get(url, cookies={'session': COOKIES_VALUE}, headers={'User-Agent': USER_AGENT})
    soup = BeautifulSoup(page.text, features="html.parser")
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
        code = part1.find_all("code")
        result = str(code[-1])[len("<code>" + "<em>"):-len("</em>" + "</code>")]
    if result == str(answer):
        return "It is working!!"
    else:
        return "Try again"

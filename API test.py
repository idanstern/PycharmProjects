import requests
from selenium import webdriver
my_driver = webdriver.Chrome()
my_driver2 = webdriver.Chrome()
import names
repos = requests.get("https://api.github.com/users/avielb/repos")
my_names = []
for i in range(3):
    if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()["age"] <= 120:
        my_names.append(i)

unis = requests.get("http://universities.hipolabs.com/search?country=Israel")
my_driver.get("https://www.ycombinator.com/")
my_driver2.get("https://hub.docker.com")
assert my_driver.title == "Y Combinator"
assert my_driver2.title == "Docker Hub Container Image Library | App Containerization"
assert len(repos.json()) > 5
assert len(my_names) == 0
assert len(unis.json()) > 5
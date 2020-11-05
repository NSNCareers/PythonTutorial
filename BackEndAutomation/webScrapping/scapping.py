import requests
from bs4 import BeautifulSoup


data = requests.get("http://qa.loginapp.nsncareers.com/Identity/Account/Register")
soup = BeautifulSoup(data.content, "html.parser")
inputField = soup.find("input", {"type": "email"})
print(inputField.prettify())


if __name__ == "__main__":
    pass
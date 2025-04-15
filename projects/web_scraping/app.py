import requests
from bs4 import BeautifulSoup as bs


inputForGitUser = input("Enter Your GitHub Username :")
git_url = f"https://github.com/{inputForGitUser}"
getReq = requests.get(git_url)
bSoup = bs(getReq.content,"html.parser")
profileImg = bSoup.find("img",{"class","avatar"})["src"]
print(profileImg)
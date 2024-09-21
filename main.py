from bs4 import BeautifulSoup

with open('following.html', 'r', encoding='utf-8') as file:
    following = file.read()
with open('follower.html', 'r', encoding='utf-8') as file:
    follower = file.read()

for_following = BeautifulSoup(following, 'html.parser')
for_follower = BeautifulSoup(follower, 'html.parser')

spans_following = for_following.find_all('span', class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
ids_following = [span.text.strip() for span in spans_following]

spans_follower = for_follower.find_all('span', class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
ids_follower = [span.text.strip() for span in spans_follower]

for id_following in ids_following:
    if id_following not in ids_follower:
        print(id_following)

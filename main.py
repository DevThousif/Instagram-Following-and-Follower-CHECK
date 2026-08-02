from bs4 import BeautifulSoup

with open('following.html', 'r', encoding='utf-8') as file:
    following = file.read()
with open('follower.html', 'r', encoding='utf-8') as file:
    follower = file.read()

for_following = BeautifulSoup(following, 'html.parser')
for_follower = BeautifulSoup(follower, 'html.parser')

# Match spans that start with _ap3a _aaco (Instagram username spans)
spans_following = for_following.find_all('span', class_=lambda x: x and x.startswith('_ap3a _aaco'))
spans_follower = for_follower.find_all('span', class_=lambda x: x and x.startswith('_ap3a _aaco'))

ids_following = [span.text.strip() for span in spans_following]
ids_follower = [span.text.strip() for span in spans_follower]

# Find accounts you follow that don't follow you back
not_following_back = [user for user in ids_following if user not in ids_follower]

# Print to console
for user in not_following_back:
    print(user)

# Save to text file
with open('not_following_back.txt', 'w', encoding='utf-8') as f:
    for user in not_following_back:
        f.write(user + '\n')

print(f"\nDone! Found {len(not_following_back)} accounts not following you back.")
print("Results saved to not_following_back.txt")
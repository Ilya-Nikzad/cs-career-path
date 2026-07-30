# Task 1: Open an online text file using urllib.request.urlopen() and print every line.
#BEGIN
import urllib.request

from bs4 import BeautifulSoup

text_1 = "https://data.pr4e.org/romeo.txt"
response = urllib.request.urlopen(text_1)
data = response.read().decode('utf8')
#print(html)
#END


# Task 2: Download a text file, decode each line,
# split it into words, and count word frequencies using a dictionary.
#BEGIN
import urllib.request

text_2 = "https://data.pr4e.org/romeo.txt"
response = urllib.request.urlopen(text_2)
data_v = response.read().decode('utf8')
dict_count = {}
for line in data_v.splitlines():
    parts = line.split()
    for part in parts:
        if part in dict_count:
            dict_count[part] += 1
        else:
            dict_count[part] = 1
for key, value in dict_count.items():
    print(key, value)
#END
# Method 2:
import urllib.request

text_3 = "https://data.pr4e.org/romeo.txt"
response = urllib.request.urlopen(text_3)

dict_count = {}

for line in response:
    line = line.decode("utf8")
    for word in line.split():
        dict_count[word] = dict_count.get(word, 0) + 1

for key, value in dict_count.items():
    print(key, value)
#END


# Task 3: Downloads an HTML page.
# Prints its HTML source.
# Finds all hyperlinks (href values).
# Downloads each linked page.
#Begin
import urllib.request

from bs4 import BeautifulSoup

page_url = "https://example.com"
response = urllib.request.urlopen(page_url)
html_text = response.read().decode("utf8")
soup = BeautifulSoup(html_text, "lxml")
href_list = []
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    href_list.append(href)
# Download each linked page
print(href_list)
for url in href_list:
    if url:
        try:
            linked_response = urllib.request.urlopen(url)
            linked_html = linked_response.read().decode("utf8")
            print(linked_html)

        except Exception as e:
            print("Could not download:", url, e)







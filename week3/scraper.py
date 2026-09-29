import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "test"}

# url = "https://ru.wikipedia.org/wiki/Левитт,_Сол"
url = "https://en.wikipedia.org/wiki/Sol_LeWitt"

response = requests.get(url, headers=headers)

print(response.status_code)
print(len(response.text))
print(response.text[:400])

soup = BeautifulSoup(response.text, "html.parser")

print()
print(f"главный заголовок: {soup.title.text}")
print()

paragraphs = soup.find_all("p")
for p in paragraphs[:5]:
    print(p.get_text().strip()[:200])
    print("---" * 10)

image_urls = []
for img in soup.find_all("img"):
    src = img.get("src", "")
    if ".jpg" in src.lower():
        if src.startswith("//"):
            src = "https:" + src
        image_urls.append(src)

for img in image_urls:
    print(img)
    print()


links = []

for a in soup.find_all("a"):
    # if a.get("href", "").startswith('/wiki/'):
    #     lang_link = url.split(".")[0]
    #     href = lang_link + "." + "wikipedia.org" + a.get("href")
    #     links.append(href)

    href = a.get("href", "")
    if href.startswith("https://en.") \
        or href.startswith("https://ru."): # обратный слеш - перенос строки кода!
        lang_link = url.split(".")[0]
        links.append(href)

print(f"ссылок на статьи: {len(links)}")

# for link in links:
#     print(link)
#     print()


links_txt = "\n".join(links)

with open("week3/wiki_links.txt", "w", encoding="utf-8") as f:
    f.write(links_txt)


print("done!")
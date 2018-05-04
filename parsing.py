import requests

index_url, url, urls = 'https://moikrug.ru/', str(), []
domain, response = index_url[8:len(index_url)], requests.get(index_url)
content = response.text
for i in range(len(content)):
    if content[i:i + 8] == 'https://':
        for j in range(i, len(content)):
            if content[j] != '"':
                url = url + content[j]
            else:
                urls.append(url)
                url = ''
                break
for url in urls:
    if url.find(domain) > -1:
        urls.remove(url)

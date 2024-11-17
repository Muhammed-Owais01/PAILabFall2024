def convertUrl(url):
    url = url.replace("http://www.", "")
    return url + ".com"
print(convertUrl(input("Enter url with http://www.: ")))
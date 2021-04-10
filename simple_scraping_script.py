import requests
from bs4 import BeautifulSoup

def statusCode():
    print("Status code: " + str(result.status_code))
    print("\n")

def aTags():
    for a_tag in soup.find_all('a'):
        print(a_tag)

def pTags():
    for p_tag in soup.find_all('p'):
        print(p_tag)

def h1Tags():
    for h1_tag in soup.find_all('h1'):
        print(h1_tag)

def h2Tags():
    for h2_tag in soup.find_all('h2'):
        print(h2_tag)

def h3Tags():
    for h3_tag in soup.find_all('h3'):
        print(h3_tag)

def source():
    print(soup.prettify())

print("Starting Simple Scraping Script...")
url = input("Enter/Paste the URL address in the following format 'https://www.example.com': ")
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'html.parser')
print("\n")

while True:
    print("Possible actions: ")
    print("1. Status Code")
    print("2. A Tags")
    print("3. P Tags")
    print("4. H1 Tags")
    print("5. H2 Tags")
    print("6. H3 Tags")
    print("7. Structured Source-code")
    print("0. Exit")

    opt = int(input("Enter the number of your choice "))
    if opt == 1:
        statusCode()

    elif opt == 2:
        aTags()

    elif opt == 3:
        pTags()

    elif opt == 4:
        h1Tags()

    elif opt == 5:
        h2Tags()

    elif opt == 6:
        h3Tags()

    elif opt == 7:
        source()

    elif opt == 0:
        print("Good bye!!!")
        break

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/intro.html#scripting-in-the-python-console",
    timeout=15
)
response.raise_for_status()

print(f"{response.status_code}: Success")



print()

soup = BeautifulSoup(response.text, "html.parser")

main_content = soup.find("div", attrs={"itemprop": "articleBody"}) # find a div element whose itemprop attrs equals articlebody



#Check if main content does exist
if not main_content:
    raise Exception("Main content empty")

unwanted = main_content.find("nav", id="contents")

#Check that unwanted exists 
try:
    unwanted.decompose()

except NameError:

    print(f"{True}, There was an error")
else:
    print(f"{False}, There was no error")

""" unwanted = main_content.find("nav", id="contents")

if unwanted is not None:
    unwanted.decompose()
"""

print()
""" 
for trash in unwanted:
    trash.decompose() """


print("Decomposed: ",unwanted.decomposed)

print()

#find the header links and remove them
""" headerlink = main_content.find('a', class_='headerlink')

if headerlink:
    headerlink.decompose()

else:
    raise Exception("Headers don't exist") """


#get headers from main content
headers = main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], limit=5)

#get paragraphs
paragraphs = main_content.find_all("p", limit=5)


#finding header elements
for header in headers:
    #find all achor tags inside the header
    links = header.find_all('a', class_='headerlink')
    for link in links:
        link.decompose()
    print(header.get_text())
    print()

#finding paragraph
for para in paragraphs:
    print(para.get_text())

print()



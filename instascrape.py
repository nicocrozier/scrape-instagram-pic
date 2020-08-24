import requests
import shutil
from bs4 import BeautifulSoup
import html5lib
from datetime import date
import random

# Set name for downloaded photo. Date + a random number
name = str(date.today()) + str(random.randint(1, 100000))

# Ask for user input
get_url = input("Enter URL:")


# Open request. Find image in the DOM.
resp = requests.get(get_url, stream=True)
soup = BeautifulSoup(resp.content, 'html5lib')
meta = soup.find("meta", property="og:image").get('content')

# Re open request with new URL
resp = requests.get(meta, stream=True)


# Open a local file with wb ( write binary ) permission.
local_file = open('%s.jpg' % name, 'wb')
# Set decode_content value to True.
# otherwise the downloaded image file's size will be zero.
resp.raw.decode_content = True
# Copy the response stream raw data to local image file.
shutil.copyfileobj(resp.raw, local_file)
# Remove the image url response object.
del resp

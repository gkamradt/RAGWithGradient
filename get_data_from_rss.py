import xml.etree.ElementTree as ET
import requests

# URL of the XML data
url = "https://buttondown.email/ainews/rss"

# Fetch the XML data
response = requests.get(url)
xml_data = response.text

# Parse the XML
root = ET.fromstring(xml_data)

# Function to recursively extract text from the XML tree
def extract_text(element):
    text = ''
    if element.text:
        text += element.text.strip() + ' '
    for child in element:
        text += extract_text(child)
    if element.tail:
        text += element.tail.strip() + ' '
    return text

# Extract text from the root element
text_content = extract_text(root)

with open("data/ai_news_rss.txt", "w") as file:
    file.write(text_content)
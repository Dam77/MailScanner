from utils import read_txt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, 'url.txt')


read = read_txt(file_path)

urls = []
for url in read:
    url = url.strip()
    urls.append(url)
# urls returns a list of URLs

# Now we will create a dictionary to store the emails
emails_per_url = {}
for index, url in enumerate(urls):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    texte = soup.get_text()
    # Now texte contains all the text from the HTML page
    
    # Now we will get a list of all words
    words = texte.split()
    mails = []
    for word in words:
        if '@' in word:
            for char in [',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\']:
                word = word.replace(char, '')
            mails.append(word)
    emails_per_url[f'mail_{index+1}'] = mails


# All emails are now in a dictionary
# But the problem is all columns do not have the same length
# So we will create a DataFrame manually

df = pd.DataFrame()

for key, value in emails_per_url.items():
    df[key] = pd.Series(value)

emails_path = os.path.join(base_path, 'emails.csv')
df.to_csv(emails_path, index=False)



    


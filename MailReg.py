# import requests
# import json
# from bs4 import BeautifulSoup
#
# # response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox')
# # mail = response.json()
# # print(mail[0])
# #
# # # login = mail.split('@')[0]
# # # domain = mail.split('@')[1]
# # #
# # # z6ba9acm9s3@icznn.com
#
# # mail = 'z6ba9acm9s3@icznn.com'
# mail = '1vjecp76ex@icznn.com'
#
# login = mail.split('@')[0]
# domain = mail.split('@')[1]
#
# response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
#
# messages = response.json()
# print(messages[0]['id'])
# meskey = messages[0]['id']
#
# # [{'id': 109750380, 'from': 'masanec@bk.ru', 'subject': 'test', 'date': '2023-06-04 23:07:09'}]
# response = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={meskey}')
# text = response.json()
# print(text['body'])
# # # readtext = text['p[]']
# soup = BeautifulSoup(text['body'], 'html.parser')
# print(soup.p.text)
# soupp = soup.p.text.split(': ')[1].strip()
# print(soupp)
# souppp = list(soupp)
# print(souppp)



# print(readtext)
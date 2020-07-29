import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

url = 'https://discuss.codecademy.com/c/get-help/javascript/1817'
response = requests.get(url)
html_doc = response.text 
html_soup = BeautifulSoup(response.text, 'html.parser')

# print(response.text[:500])

question_containers = html_soup.find_all('tr', class_ = 'topic-list-item')
# print(question_containers)

question_one = question_containers[2]

print(question_one)

question_one_name = question_one.a.text

print(question_one_name)

question_one_tags = question_one.find_all('div', class_='discourse-tags')
question_one_categories = question_one.find_all('span', class_='category-name')
question_one_views = question_one.find('span', class_='views').text
question_one_replies = question_one.find('td', class_='replies').text

# print(question_one_replies)

for i in question_one_tags:
    print (i.text)

for i in question_one_categories:
    print (i.text)




names = []
tags = []
temp_tags = []
categories = []
temp_categories = []
views = []
temp_views = []
num_replies = []
temp_num_replies = []

for container in question_containers:

	name = container.a.text
	names.append(name)

	tag = container.find_all('div', class_='discourse-tags')
	category = container.find_all('span', class_='category-name')
	view = container.find('span', class_='views').text
	num_reply = container.find('td', class_='replies').text

	views.append(view)
	temp_views.append(view)

	num_replies.append(num_reply)
	temp_num_replies.append(num_reply)

	for i in tag:
		tags.append(i.text)
		temp_tags.append(i.text)

	for j in category:
		categories.append(j.text)
		temp_categories.append(j.text)



	print("", name, "----------------------", temp_tags, "----------------------", temp_categories, "----------------------", temp_views, "----------------------", temp_num_replies)
	print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

	temp_tags = []
	temp_categories = []
	temp_views = []
	temp_num_replies = []

csv = pd.DataFrame({
	'Title': names, 'Tags': tags, 'Views': views, 'Number of Replies': num_replies
})

csv.to_csv('GetHelp-Java.csv')
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup


names = []
categories = []
tags_array = []
replies = []
posts = []
comments_array = []
views = []

for i in range(0, 2):

    URL = 'https://discuss.codecademy.com/c/get-help/javascript/1817?page='+str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    containers = soup.find_all(class_='topic-list-item')


    for container in containers:

        topic = container.find('a', class_='title')
        url_temp = topic['href']
        page_temp = requests.get(url_temp)
        soup_temp = BeautifulSoup(page_temp.content, 'html.parser')

        container_temp = soup_temp.find_all(class_='post')

        comments = ''
        for i in container_temp[1:]:
            comments += i.text

        tag = container.find_all('a', class_='discourse-tag')
        tags = ''
        for t in tag:
            tags += t.text+','
        tags = tags.rstrip(',')

        view = container.find('span', class_='views').text
        views.append(view)

        reps = container.find('td', class_='replies')
        names.append(topic.text)
        categories.append("Get Help - Java")
        tags_array.append(tags)
        replies.append(reps.span.text)
        posts.append(container_temp[0].text)
        comments_array.append(comments)

csv = pd.DataFrame({'Name': names, 'Categories': categories,
                    'Tags': tags_array, 'Replies': replies, 'Views':views,
                    'Post': posts, 'Comments': comments_array})

csv.to_csv('getHelpJavaDataset.csv')
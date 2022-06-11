# -*- encoding = utf-8 -*-
import requests
from lxml import etree
import time
import csv
import random

url = 'https://www.python.org/jobs/'
headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
    }
response = requests.get(url, headers=headers).content.decode('utf-8')
p = etree.HTML(response)
a_list = p.xpath("//*[@id='content']/div/section/div")
items = {}
for a in a_list:
    JobTitle = a.xpath('//*[@class="listing-company-name"]/a/text()')[0]
    if JobTitle:
        items["JobTitle"] = JobTitle
    else:
        items["JobTitle"] = None

    DetailUrl = 'https://www.python.org' + a.xpath('.//@href')[0]
    if DetailUrl:
        items["DetailUrl"] = DetailUrl
    else:
        items["DetailUrl"] = None

    detail_page_text = requests.get(url=DetailUrl, headers=headers).content.decode('utf-8')
    detail_tree = etree.HTML(detail_page_text)

    Company = a.xpath('//*[@id="content"]/div/section/div/ol/li/h2/span/text()[3]')[0]

    if Company:
        items["Company"] = Company
    else:
        items["Company"] = None

    FromWhere = detail_tree.xpath('//*[@id="content"]/div/section/article/div/ul/li[3]/a/text()')
    if FromWhere:
        items["FromWhere"] = FromWhere
    else:
        items["FromWhere"] = None

    PostDate = a.xpath('//*[@class="listing-posted"]/time/text()')[0]
    if PostDate:
        items["PostDate"] = PostDate
    else:
        items["PostDate"] = None

    Location = a.xpath('//*[@class="listing-location"]/a/text()')[0]
    if Location:
        items["Location"] = Location
    else:
        items["Location"] = None

    CrawledTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if CrawledTime:
        items["CrawledTime"] = CrawledTime
    else:
        items["CrawledTime"] = None

    time.sleep(random.randint(0, 1))
    with open('python.org.csv', 'a') as fp:
        csv_writer = csv.writer(fp)
        csv_writer.writerow([JobTitle, DetailUrl, Company, FromWhere, PostDate, Location, CrawledTime])


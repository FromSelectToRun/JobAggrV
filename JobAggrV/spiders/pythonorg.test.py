# -*- encoding = utf-8 -*-
import requests
from lxml import etree
import time
import csv
import random
class xpath(object):
    # 初始化url
    def __init__(self):
        self.url = "https://www.python.org/jobs/?page={}"
        self.blog = 1
    #主函数
    def get_heml(self, url):
        url = 'https://www.python.org/jobs/'
        self.blog += 1
        url = 'https://www.python.org/jobs/'
        headers = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',

            }
        response = requests.get(url, headers=headers).content.decode('utf-8')
        p = etree.HTML(response)
        a_list = p.xpath('//*[@id="content"]/div/section/div/ol/li')
        items = {}
        for a in a_list:
            JobTitle = a.xpath('.//*[@class="listing-company-name"]/a/text()')[0]
            if JobTitle:
                items["JobTitle"] = JobTitle
            else:
                items["JobTitle"] = None
            DetailUrl = 'https://www.python.org' + a.xpath('.//*[@class="listing-company-name"]//@href')[0]
            if DetailUrl:
                items["DetailUrl"] = DetailUrl
            else:
                items["DetailUrl"] = None
            detail_page_text = requests.get(url=DetailUrl, headers=headers).content.decode('utf-8')
            detail_tree = etree.HTML(detail_page_text)
            FromWhere = detail_tree.xpath('//*[@id="content"]/div/section/article/div/ul/li[3]/a/text()')
            if FromWhere:
                items["FromWhere"] = FromWhere
            else:
                items["FromWhere"] = None
            Company = detail_tree.xpath('.//*[@id="content"]/div/section/article/h1/span[1]/span/text()[3]')
            if Company:
                items["Company"] = Company
            else:
                items["Company"] = None
            PostDate = a.xpath('//*[@class="listing-posted"]/time/text()')[0]
            if PostDate:
                items["PostDate"] = PostDate
            else:
                items["PostDate"] = None
            Location = a.xpath('.//*[@class="listing-location"]/a/text()')[0]
            if Location:
                items["Location"] = Location
            else:
                items["Location"] = None
            CrawledTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            if CrawledTime:
                items["CrawledTime"] = CrawledTime
            else:
                items["CrawledTime"] = None
            time.sleep(random.randint(0,1))
            with open('python.org.csv', 'a') as fp:
                csv_writer = csv.writer(fp)
                csv_writer.writerow([JobTitle, DetailUrl, Company, FromWhere, PostDate, Location, CrawledTime])
                print(items)

    def run(self):
        # 页的信息
        for pg in range(1,100):
            # 将页码数嵌入url中
            url = self.url.format(pg)
            # 调用主方法
            self.get_heml(url)
            # 设置间隔，休眠0或1秒，目的是反爬
            time.sleep(random.randint(0, 1))
            self.blog = 1

if __name__ == "__main__":
    spider = xpath()
    spider.run()
print('完毕！')

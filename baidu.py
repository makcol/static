import json
import requests
from lxml import etree

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Host': 'top.baidu.com',
    'Upgrade-Insecure-Requests': '1',
}
# 获取百度热榜
bd_hot_url = 'https://top.baidu.com/board?tab=novel'
response = requests.get(bd_hot_url, headers=headers)
html = etree.HTML(response.text)
bd_hot_block = html.xpath("//div[contains(@class,'category-wrap_iQLoo')]")
book_list = []
for single in bd_hot_block:
    book = {}
    # 获取标题
    title = single.xpath('string(.//div[@class="c-single-text-ellipsis"]/text())')
    print('标题是：{}'.format(title))
    book['title'] = title
    # 小说获取作者
    author = single.xpath('string(.//div[@class="intro_1l0wp"]/text())')
    print('作者是：{}'.format(author))
    book['author'] = author
    # # 获取链接
    # url = single.xpath('string(./a/@href)')
    # print('链接是：{}'.format(url))
    # 获取热搜排名
    rank = single.xpath('string(./a/div/text())')
    print('排名是：{}'.format(rank))
    book['rank'] = rank
    # 获取图片地址
    pic = single.xpath('string(./a/img/@src)')
    print('图片地址是：{}'.format(pic))
    book['pic'] = pic
    # 获取热搜指数hot-index
    zhishu = single.xpath('string(.//div[contains(@class,"hot-index_1Bl1a")]/text())')
    print('热搜指数是：{}'.format(zhishu))
    book['zhishu'] = zhishu
    # 获取简介hot-desc
    desc = single.xpath('string(.//div[contains(@class,"desc_")]/text())')
    print('描述是：{}'.format(desc))
    book['desc'] = desc
    book_list.append(book)

output_json = json.dumps(book_list)
print(output_json)
file = open("book.json","w")
file.write(output_json)
file.close()
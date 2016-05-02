import urllib2
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from stack.items import StackItem
import cfscrape


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 ' 
             #'(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'


def download(url, path, referer=None, cookie=None):
    req = urllib2.Request(url)
    if referer:
        req.add_header("Referer", referer)
    if cookie:
        req.add_header("Cookie", cookie)
    req.add_header("User-Agent", USER_AGENT)
    u = urllib2.urlopen(req)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print u"Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        _buffer = u.read(block_sz)
        if not _buffer:
            break

        file_size_dl += len(_buffer)
        f.write(_buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status += chr(8) * (len(status) + 1)
        print status,

    f.close()


class StackSpider(CrawlSpider):
    name = 'stack'
    start_urls = [
        'https://boerse.to'
    ]
    allowed_domains = ['https://boerse.to', ]
    rules = (
        Rule(SgmlLinkExtractor(allow=(r'page\.php\?id=\d+$',)), callback='parse_item'),
    )

    def parse_start_url(self, response):
        self.cookie = response.headers.get('Set-Cookie').split(';', 1)[0]
        return super(Spider, self).parse_start_url(response)

    def parse_item(self, response):
        sel = Selector(response)
        image_url = sel.xpath('//img/@src').extract()[0]
        return download(image_url, path, response.url, self.cookie)

    def start_requests(self):
      cf_requests = []
      for url in self.start_urls:
          token, agent = cfscrape.get_tokens(url, USER_AGENT)
          #token, agent = cfscrape.get_tokens(url)
          cf_requests.append(scrapy.Request(url=url, cookies={'__cfduid': token['__cfduid']}, headers={'User-Agent': agent}))
          print "useragent in cfrequest: " , agent
          print "token in cfrequest: ", token
      return cf_requests

'''
from scrapy import Spider
from selenium import webdriver

from stack.items import StackItem


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'



class StackSpider(Spider):
	name = "stack"
	allowed_domains = [
	"https://boerse.to"]

	start_urls = [

		"https://boerse.to"
	]

	def __init__(self):
		#self.driver = webdriver.PhantomJS()
		self.driver = webdriver.Firefox()

	def parse_start_url(self, response):
		self.cookie = response.headers.get('Set-Cookie').split(';')[0]
		return super(Spider, self).parse_start_url(response)

	def parse(self, response):
		item = StackItem()
		self.driver.get(response.url)
		item['title'] = self.driver.find_elements_by_class_name('inner').text
		item['url'] = self.driver.find_elements_by_class_name('inner').text
		yield item

		# get colors
        '''

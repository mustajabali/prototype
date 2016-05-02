import scrapy

from scrapy.spider import BaseSpider
#from scrapy.selector import Selector
#from selenium import webdriver

from stack.items import StackItem


#from scrapy.selector import Selector
#import requests
import cfscrape
#from requests import Request


#sess.mount("http://", cfscrape.CloudflareAdapter())
#sess.mount("https://", cfscrape.CloudflareAdapter())



USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'

class StackSpider(BaseSpider):
	name = "stack"
	allowed_domains = [
	"boerse.to"]

	start_urls = [
		"https://boerse.to/"
	]

	#def __init__(self):
	#	self.driver = webdriver.PhantomJS()
	'''
	def parse_start_url(self, response):
		self.cookie = {'cf_clearance': 'e49068ee588706fdabc0c434eb66df533d12ec3c-1461787949-86400', '__cfduid': 'dda7da5497ba77c6063e79d48921df0a71461787944'}
		return super(Spider, self).parse_start_url(response)
	'''

	def start_requests(self):
		cf_requests = []
		for url in self.start_urls:
			token, agent = cfscrape.get_tokens(url, "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36")
			
			
			cf_requests.append(scrapy.Request(url=url,
				cookies=token,
				headers={'User-Agent': agent}))
			return cf_requests

	def parse(self, response):
		print "#####Parsing Hello World"
		item = StackItem()
		#self.driver.get(response.url)
	
	#	self.driver.close()
		return item

		
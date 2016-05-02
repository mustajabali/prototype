from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

''' "stackoverflow.com", '''
''' 
		"http://stackoverflow.com/questions?pagesize=50&sort=newest",
		'''
class StackSpider(Spider):
	name = "stack"
	allowed_domains = [
	"boerse.to"]

	start_urls = [

		"http://boerse.to/"
	]

	def parse(self, response):
		loginBtn = Selector(response).xpath('//*[@id="SignupButton"]')
		item = StackItem()
		item['title'] = loginBtn.xpath(

			'//*[@id="SignupButton"]/a/text()').extract()[0]
		item['url'] = loginBtn.xpath(
			'//*[@id="SignupButton"]/a/@href').extract()[0]
		yield item
		'''
		questions = Selector(response).xpath('//div[@class="summary"]/h3')

		for question in questions:
			item = StackItem()
			item['title'] = question.xpath(
				'a[@class="question-hyperlink"]/text()').extract()[0]
			item['url'] = question.xpath(
				'a[@class="question-hyperlink"]/@href').extract()[0]
			yield item

		'''


from scrapy.spider import Spider

class shopSpider(Spider):
	name = "shop"
	allowed_domains = ["dota2shop.cn"]
	start_urls = [
		"http://www.dota2shop.cn/?h=%E6%96%AF%E6%B8%A9",
		"http://www.dota2shop.cn/?h=%E6%96%AF%E6%B8%A9"
	]

	def parse(self, response):
		filename = response.url,split("/")[-2]
		open(filename,'wb').write(response.body)
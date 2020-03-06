import scrapy

class FollowingSpider(scrapy.Spider):
	name = 'followingspider'

	def __init__(self, follower_page, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.start_urls = [follower_page]

	def parse(self, response):
		for name in response.css('.display-name'):
			yield {'addr': name.css('span::text')[1].get().strip()}

		for href in response.css('nav.pagination > span.page > a[rel=next]::attr(href)'):
			yield response.follow(href.get(), callback=self.parse)
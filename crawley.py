import scrapy

'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'text': quote.css('span.text::text').extract_first(),'author': quote.xpath('span/small/text()').extract_first(),}

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
'''

class Spidey(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=67059303301834130',]

    def parse(self, response):
        for quote in response.xpath("//div/form"):
            yield {'yyyy': quote.xpath('div[contains(@id, "MainBox")]/div[contains(@id, "MainContent")]/div[contains(@id, "TopBox")]').extract()}

        for quote in response.xpath("//div/form"):
            yield {'xxxx': quote.xpath('div[contains(@id, "MainBox")]/div[contains(@id, "MainContent")]/div[contains(@id, "TopBox")]/node()').extract()}
            #//*[@id="TopBox"]/div[2]

        for quote in response.xpath('table'):
            yield {'zzzz': quote.xpath('()').extract()}

        for quote in response.xpath("//div/form"):
            #yield {'script': quote.xpath("script").extract()}
            pass

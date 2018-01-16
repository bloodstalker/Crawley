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
        for quote in response.css('div'):
            #yield {'data': quote.css('span')}
            yield {'data': quote.xpath('span/div/text()').extract_first(), 'data2': quote.css('span.s').extract_first()}
            #yield {'data': quote.css('span.s.div.pn')}

        for quote in response.xpath("//div/form"):
            #yield {'data3': quote.xpath("div/text()")}
            yield {'data3': quote.xpath("div").extract_first(), 'data4': quote.xpath("script").extract_first()}

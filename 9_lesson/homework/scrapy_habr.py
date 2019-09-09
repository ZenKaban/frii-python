import scrapy
import socket
import socks
import credentials

class HabrSpider(scrapy.Spider):
    name = 'habr'
    
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'}
    
    socks.set_default_proxy(socks.HTTP, credentials.proxy_address,
                            credentials.port, True, credentials.login,
                            credentials.password)
    temp = socket.socket
    socket.socket = socks.socksocket

    start_urls = [
        'https://habr.com/ru/users/afiskon/posts/',
        ]

    def parse(self, response):
        list_of_posts_urls = response.css('a.btn.btn_x-large.btn_outline_blue.post__habracut-btn::attr("href")').getall()
        for post in list_of_posts_urls:
            yield scrapy.Request(url=post, callback=self.get_posts_urls)
        
        next_page = response.css('a.arrows-pagination__item-link.arrows-pagination__item-link_next::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
    
    def get_posts_urls(self, response):

        yield {
            response.css('span.post__title-text::text').get(): response.css(
                'div.post__text.post__text-html.js-mediator-article').getall(),
            }


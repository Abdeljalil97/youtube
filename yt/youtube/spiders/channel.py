# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from youtube.items import YoutubeItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChannelSpider(scrapy.Spider):
    name = 'channel'

    def start_requests(self):
        url = 'https://www.youtube.com/channel/UCDRIjKy6eZOvKtOELtTdeUA'
        yield SeleniumRequest(
    url=url,
    callback=self.about_page,
        screenshot=True,
    script='window.scrollTo(0, document.body.scrollHeight);',
)
    def about_page(self,response):

        driver = response.meta['driver']
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/tp-yt-app-toolbar//tp-yt-paper-tab[6]"))
        )
        element.click()
        url = driver.current_url
        yield SeleniumRequest(
    url=url,
    callback=self.parse,
        screenshot=True,
    script='window.scrollTo(0, document.body.scrollHeight);',
)




    def parse(self, response):
        l = ItemLoader(item=YoutubeItem(), response=response)
        l.add_xpath('channel_name','(//div[@id="text-container"]/yt-formatted-string[@id="text"])[1]/text()')
        l.add_value('channel_url', response.url.replace('/about',''))
        l.add_xpath('description',"//div[@id='contents']//div[@id='contents']//yt-formatted-string[@id='description']/text()")
        l.add_xpath('location',"(//div[@id='contents']//div[@id='contents']//div[@id='details-container']//yt-formatted-string)[6]/text()")

        return l.load_item()

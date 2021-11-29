#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy


# In[2]:


from scrapy import Spider
from scrapy.crawler import CrawlerProcess


class NAP(Spider):
    name = 'Net_a_Porter'
    start_urls = [
        'http://www.net-a-porter.com/en-in/shop/clothing/tops',
        'https://www.net-a-porter.com/en-in/shop/shoes'
    ]
    
    def parse(self,response):
        
        for product in response.css('div.ProductListingPage52'):
            for products in response.css('div.ProductItem24'):
            
               
                yield {
                
                    #'content':product.css('div.ProductItem24__content').getall(),
                    'name ' :products.css('span.ProductItem24__name::text').get(),
                    'brand': products.css('span.ProductItem24__designer::text').get(),
                    'original_price':products.css('div.PriceWithSchema9.ProductItem24__price span.PriceWithSchema9__value span::text').getall(),
                    'image_url':products.css('div.Image18__imageContainer img::attr(src)').extract(),
                    'product_category':product.css('h1.Header6__title::text').get(),
                    #'product_page_url'== product.css('')
                    #'sale_price':prices.css('div.SingleBadge2__badge ProductItem24__badge').getall(),
                }
      
                    
        
        next_page = response.css('a.Pagination7__next').attrib['href']
        if next_page is not None:
            
            yield response.follow(next_page, callback = self.parse)
        
        
        
                
                
      
                
                
            
            
       
                
        
            
            
process = CrawlerProcess()
process.crawl(NAP)
process.start()


# In[ ]:





# In[ ]:





# In[ ]:





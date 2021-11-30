#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy


# In[2]:


from scrapy import Spider
from scrapy.crawler import CrawlerProcess


data=[]


class NAP(Spider):
    name = 'Net_a_Porter'
    start_urls = [
        'http://www.net-a-porter.com/en-in/shop/clothing/tops',
        'https://www.net-a-porter.com/en-in/shop/shoes'
    ]
    
    data.clear()
    
    def parse(self,response):
        
        for product in response.css('div.ProductListingPage52'):
            for products in response.css('div.ProductItem24'):
                
                ele={
                
                    #'content':product.css('div.ProductItem24__content').getall(),
                    'name ' :products.css('span.ProductItem24__name::text').get(),
                    'brand': products.css('span.ProductItem24__designer::text').get(),
                    'original_price':products.css('div.PriceWithSchema9.ProductItem24__price span.PriceWithSchema9__value span::text').getall(),
                    'image_url':products.css('div.Image18__imageContainer img::attr(src)').extract(),
                    'product_category':product.css('h1.Header6__title::text').get(),
                    #'product_page_url'== product.css('')
                    'sale_price':products.css('div.PriceWithScema9.ProductItem24__price div.SingleBadge2__badge ProductItem24__badge::text').getall(),
                }
                
                data.append(ele)
            
                yield ele
      
                    
        
        next_page = response.css('a.Pagination7__next').attrib['href']
        if next_page is not None:
            
            yield response.follow(next_page, callback = self.parse)
        
        
        
                

process = CrawlerProcess()
process.crawl(NAP)
process.start()
print(data)


# In[22]:


import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://Nishad_Chaoji:abcde@cluster0.ltt9k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.database


# In[23]:


for element in data:
    rec_id1 = db.nishad.insert_one(element)
    


# In[24]:


cursor = db.nishad.find()
for record in cursor:
    print(record)


# In[25]:


#Q1 Total no of items scraped
db.nishad.count_documents({})


# In[7]:


#Q2
#The Discounts for blackfriday have been removed so unable to solve


# In[8]:


# Q3
#The Discounts for blackfriday have been removed so unable to solve


# In[26]:


# Q4 Distnct Brands
len(db.nishad.distinct("brand"))


# In[10]:


# Q5
#The discounts for blackfriday have been removed so unable to solve


# In[11]:





# In[27]:


#Q6 
query = { "name": { "$regex": 'shirt', "$options" :'i' } }
docs = db.nishad.count_documents( query )
#print ( query)
print ("$regex using 'shirt' -- total:", docs, "\n")

#not working 


# In[15]:


#Q7 
#The Discounts for blackfriday have been removed so unable to solve


# In[16]:


#Q8 
#The Discounts for blackfriday have been removed so unable to solve


# In[17]:


#Q9
#The Discounts for blackfriday have been removed so unable to solve


# In[18]:


#Q10
#Unable to solve 


import scrapy
import json

class SurfboardempireSpider(scrapy.Spider):
    name = "surfboardempire"
    allowed_domains = ["surfboardempire.com.au"]
    start_urls = ["https://surfboardempire.com.au/products.json?page=1"]

    def parse(self, response):
        
        # Loads the json data from the response body
        json_data = json.loads(response.body)

        # Unpack the data into a variable
        products = json_data['products']

        # For each product yield the necessary product data. 
        for product in products:
            yield{
                'sku_name': product['title'],
                'product_id': product['id'],
                'brand': product['vendor'],
                'product_url': f"https://www.surfboardempire.com.au/products/{product['handle']}",
            }

        # As long as there are products navigate to the next page recursively.
        if products:
            current_page_num = int(response.url.split('=')[1])
            next_page_url = f"https://surfboardempire.com.au/products.json?page={current_page_num + 1}"
            yield scrapy.Request(next_page_url,callback=self.parse)
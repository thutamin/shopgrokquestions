import scrapy


class TackleworldSpider(scrapy.Spider):
    name = "tackleworld"
    allowed_domains = ["tackleworldadelaide.com.au"]
    start_urls = ["https://tackleworldadelaide.com.au"]


    def parse(self, response):

        #
        sub_menu_links = response.xpath("//ul[@class='navPage-subMenu-list']/li[@class='navPage-subMenu-item']/a | //ul[@class='navPage-subMenu-list']/li[@class='navPage-subMenu-item']/div[@class='navPage-subMenu-button']/a")
        yield from response.follow_all(sub_menu_links,self.parse_sub_menu)

    def parse_sub_menu(self,response):
        
        #
        item_links = response.xpath("//li[@class='product']//div[@class='card__buttons']/a[1]")
        yield from response.follow_all(item_links,self.parse_products)
    
    
    def parse_products(self,response):

        # helper function
        def extract_with_xpath(query):
            return response.xpath(query).get(default="").strip()

        # 
        yield{
            "sku_num":extract_with_xpath("(//dd[@class='productView-info-value'])[1]/text()"),
            "sku_name":extract_with_xpath("//h1[@itemprop='name']/text()"),
            "image_url":response.xpath("//figure[@class='productView-image']/a/img").attrib['src'],
            "price_now":extract_with_xpath("(.//div[@class='productView-price']//span[@class='price'])[1]/text()"),
            "price_was":extract_with_xpath("(.//div[@class='productView-price']//span[@class='price price--rrp'])[1]/text()"),
            "product_url":response.url,
            "product_category":extract_with_xpath(".//ol/li[2]/a/text()"),
            "product_type":extract_with_xpath(".//ol/li[3]/a/text()"),
        }   
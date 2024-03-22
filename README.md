# shopgrokquestions

## Question 1

## Setting up the environment

#### Creating a new virtual environment for shopgrok
```bash
virtualenv --system-site-packages ~/.venvs/shopgrok
```
#### Activating the created virtual environment
```bash
. ~/.venvs/shopgrok/Scripts/activate
```
__Note: You can also use pycharm or the ```myenv``` module. Probably more popular I think. Its just that I have been using ```virutalenv``` for all my projects__ 

#### Installing scrapy and necessary dependencies
```bash
pip install scrapy==2.4 shub scrapy-crawlera google-cloud-storage scrapy-sessions
```

## Issues relating to ```scrapy===2.4```

__Downgrade the ```twisted``` version__
```bash
pip install Twisted==22.10.0
```

__To solve the ```AttributeError: module 'OpenSSL.SSL' has no attribute 'SSLv3_METHOD'``` error__
```bash
pip install pyOpenSSL==22..0.0 cryptography==38.0.4
```

__To solve the ```AttributeError: 'Selector' object has no attribute '_default_type'``` error__
```bash
pip install parsel==1.7.0
```

**Note: To solve all of the above issue in one go, just upgrade the ```scrapy``` to the latest version. But for this task, I have used ```scrapy==2.4``` as per the instructions**


### To create a new scrapy project
```bash
scrapy startproject shopgrok
```

### Navigate to the project directory
```bash
cd shopgrok
```

## Question 2

### To create a new spider
```bash
scrapy genspider tackleworld tackleworldadelaide.com.au
```

```python
import scrapy


class TackleworldSpider(scrapy.Spider):
    name = "tackleworld"
    allowed_domains = ["tackleworldadelaide.com.au"]
    start_urls = ["https://tackleworldadelaide.com.au"]


    def parse(self, response):

        # Navigates through the menu and fetches all the submenu link
        sub_menu_links = response.xpath("//ul[@class='navPage-subMenu-list']/li[@class='navPage-subMenu-item']/a | //ul[@class='navPage-subMenu-list']/li[@class='navPage-subMenu-item']/div[@class='navPage-subMenu-button']/a")
        
        # Loops through each submenu item
        yield from response.follow_all(sub_menu_links,self.parse_sub_menu)

    def parse_sub_menu(self,response):
        
        # Retrieves all the links to the product on the page
        item_links = response.xpath("//li[@class='product']//div[@class='card__buttons']/a[1]")
        
        # Loops through each product on the page
        yield from response.follow_all(item_links,self.parse_products)
    
        # Not in the task description, just Min being curious
        # try:
        #     next_page = response.xpath(".//li[@class='pagination__item  pagination__item--next']/a").attrib["href"]
        # except Exception as e:
        #     next_page = None
        # if next_page is not None:
        #     yield scrapy.Request(next_page,callback=self.parse_sub_menu)


    def parse_products(self,response):

        # helper function 
        def extract_with_xpath(query):
            return response.xpath(query).get(default="").strip()

        # For each product yield the necessary product data
        yield{
            "sku_num":extract_with_xpath("(//dd[@class='productView-info-value'])[1]/text()"),
            "sku_name":extract_with_xpath("//h1[@itemprop='name']/text()"),
            "image_url":response.xpath("//figure[@class='productView-image']/a/img").attrib['src'],
            "price_now":extract_with_xpath("(.//div[@class='productView-price']//span[@class='price'])[1]/text()"),
            "price_was":extract_with_xpath("(.//div[@class='productView-price']//span[@class='price price--rrp'])[1]/text()"),
            "product_url":response.url,
            # "product_category":extract_with_xpath(".//ol/li[2]/a/text()"),
            # "product_type":extract_with_xpath(".//ol/li[3]/a/text()"),
        }   

```


### Running the crawler and saving the results in a json file
```bash
scrapy crawl tackleworld -O tackleworld.json
```

## Question 3

### To create a new spider
```bash
scrapy genspider surfboardempire surfboardempire.com.au
```

```python
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

```


### Running the crawler and saving the results in a json file
```bash
scrapy crawl surfboardempire -O surfboardempire.json
```




## Question 4

### Navigate back to the root directory
```bash
cd ..
```
### Simply run the regex.py file
```bash
python regex.py
```

## Potential to do list on the top of my head
- add test scripts
- add cloud storage



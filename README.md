# shopgrokquestions

## Question 1

virtualenv --system-site-packages ~/.venvs/shopgrok
. ~/.venvs/shopgrok/Scripts/activate
pip install scrapy==2.4 shub scrapy-crawlera google-cloud-storage scrapy-sessions
pip install Twisted==22.10.0
pip install pyOpenSSL==22..0.0 cryptography==38.0.4
pip install parsel==1.7.0

scrapy startproject shopgrok


## Question 2
scrapy genspider tackleworld tackleworldadelaide.com.au

scrapy crawl tackleworld -O tackleworld.json


## Question 3
scrapy genspider surfboardempire surfboardempire.com.au

scrapy crawl surfboardempire -O surfboardempire.json


## Question 4



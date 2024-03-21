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

### Running the crawler and saving the results in a json file
```bash
scrapy crawl tackleworld -O tackleworld.json
```

## Question 3

### To create a new spider
```bash
scrapy genspider surfboardempire surfboardempire.com.au
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



---
title: |
  ![](./img/Logo.png){width=2in}
  "Introduction to Python modules."
date: April, 2022
lang: en-EN
urlcolor: blue
geometry: "left=2.5cm,right=2.5cm,top=3cm,bottom=3cm"
documentclass: article
fontfamily: Alegreya
author: Patrick Nsukami
abstract: Summary of this document
thanks: Acknowledgments footnote after the document title.
code-line-numbers: true
latex-output-dir: output
output-file: foo2.pdf
header-includes: |
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhf{}
    \rhead{Dakar Institute of Technology}
    \lhead{Patrick Nsukami}
    \rfoot{Page \thepage}
---


\newpage

![Figure1](img/scrapy.png)

# Scrapy
[Scrapy][1] is an [open source][2] Python framework used for extracting data from websites. It is very useful for collecting data at a large scale, automating scraping tasks, and performing data analysis.
# Why use scrapy?
Scrapy is a fast high-level [web crawling][3] and [Web scraping][4] framework, used to crawl websites and extract structured data from their pages.
# Installing Scrapy
There are [different ways ][5] to install scrapy. The easiest option is to install the [Anaconda][6] distribution. You can also install Scrapy  using pip or conda.
# Checking the installation
To check if Scrapy is properly installed on your system, you can execute the following command in your terminal:
```plaintext
scrapy version
```
This should display the version of Scrapy installed on your system. If Scrapy is installed correctly, you should see an output similar to this:

![](img/Capture.png)

# 1.  Using Scrapy 
##### Command-line interface overview

  Scrapy's [command-line][7] interface is used to execute Scrapy commands to create new projects, run spiders to extract data, and more.
##### Creating a new project
  To create a new Scrapy project, you can use :
```python
 scrapy startproject project_name
```
command in Scrapy's command-line interface .For exemple :

![Figure 2](img/caput1.png)
# 2. Structure of a Scrapy project 
In our case, here is the structure of our Jumia project.

![](img/Caput2.png)
* #####   spiders  

 The [spiders][8] stored in a folder named "spiders" are Python classes that define how to extract data from a website.
 
```python
from import scrapy , spider
class Myspider(scrapy):
    name="myspider"
    start_urls=["http://www.example.com"]
    # Extract data from the response
    def parse(self,reponse):
        title=reponse.css("title::text").get()
    # Yield an item containing the extracted data
        yield {"title": title}
```
In this example, MySpider is a spider that extracts the title of a webpage and stores the result in an item object.
* 
* ##### __init__.py
file can be empty, or it can contain Python code that needs to be executed when the package is imported. It can contain class definitions, functions, variables, constants, module imports, and so on.
* #####  items.py
[Items][9] are containers that store the data extracted by the spiders.
```python
import scrapy
class MyItem(scrapy.Item):
     title = scrapy.Field()
     description = scrapy.Field()
```
In this example, MyItem is an item object that contains title and description fields to store data extracted by a spider.
* #####  Middleware.py
[Middleware][10] are Python classes that provide additional functionality to Scrapy, such as filtering requests or processing responses.
```python
class CustomMiddleware:
    def process_request(self, request, spider):
        # Modify the request before it is sent
        request.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

    def process_response(self, request, response, spider):
        # Modify the response before it is returned to the spider
        if response.status == 404:
            return scrapy.Request("http://www.example.com", callback=spider.parse_error)
        else:
            return response
```
In this example, CustomMiddleware is a class that modifies requests and responses by adding a custom User-Agent header to requests and checking the response status code. If the status code is 404, the middleware sends a new request to another page.
* ##### Pipelines.py
 [Pipelines][11] are Python classes that handle the data extracted by the spiders.
 ```python
import json
class MyPipeline:
    def __init__(self):
        self.file = open("data.json", "w")

    def process_item(self, item, spider):
        # Write the item to a JSON file
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        # Close the file when the spider is done
        self.file.close()
```
In this example, MyPipeline is a class that stores the data extracted by a spider in a JSON file. The process_item method is called for each extracted item, which is then written to the file. The close_spider method is called when the spider has finished its work, and it closes the file.
* ##### Settings.py
[Settings][12] are configuration variables that define the behavior of Scrapy.
```python
BOT_NAME = "mybot"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {"myproject.pipelines.MyPipeline": 300}
```
In this example, Scrapy settings are defined in a settings.py file. The bot name, User-Agent header used for requests, whether to obey the robots.txt file, and the pipeline used are all specified in this file.
* ##### Scrapy.cfg
This is the main configuration file for Scrapy. It contains information such as the project name, default settings, and spider locations.
# 3. Data extraction
In our case, we will extract data on the articles from the Jumia website (https://www.jumia.com.tn)
##### * Writing in Item.py
  ```python
import scrapy
class ArticleItem(scrapy.Item):
      # Definition of fields for the ArticleItem object
      # Field for article designations
      designations=scrapy.Field()
      # Field for article images
      picture=scrapy.Field()
      # Field for article prices
      price=scrapy.Field()

```
In this code, we retrieve the designation, image, and price of an article.
* ##### Creating a spider file in the spider folder
We will create a new file "article.py" in the spider folder. In this file, we will write our spider which is nothing but a class inheriting from the Scrapy spider class.
```python
# Import necessary modules
from scrapy import Request, Spider
from ..items import ArticleItem
from jumia import items

# Create a spider class
class SpiderArticle(Spider):
    # Define spider name
    name = "article"
    # Define the URL to scrape
    url = "https://www.jumia.com.tn/"

    # Define the starting point for the spider
    def start_requests(self):
        # Send a request to the URL and specify the callback function to use
        yield Request(url=self.url, callback=self.parse_article)

    # Define the callback function to extract data from the page
    def parse_article(self, response):
        # Find all the articles on the page
        listeArticle = response.css('article.prd')
        # Loop through each article and extract relevant data
        for article in listeArticle:
            # Extract the article's designation
            designations = article.css('a.core div.name::text').extract_first()
            # Extract the article's picture
            picture = article.css('a.core img.img').attrib['data-src']
            # Extract the article's price
            price = article.css('a.core div.prc::text').extract_first()
            # Create an ArticleItem instance and fill it with data
            item = ArticleItem()
            item['designations'] = designations
            item['picture'] = picture
            item['price'] = price

            # Yield the ArticleItem instance to Scrapy for further processing
            yield item
```




  [1]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [2]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [3]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [4]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [5]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [6]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [7]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [8]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [9]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [10]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [11]: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  [12]: https://docs.scrapy.org/en/latest/topics/settings.html

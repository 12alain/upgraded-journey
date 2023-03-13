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
* #####    __ _init___.py :



  [1]: http://fr.softoware.org/apps/download-scrapy-for-web.html
  [2]: https://github.com/scrapy/scrapy
  [3]: https://en.wikipedia.org/wiki/Web_crawler
  [4]: https://en.wikipedia.org/wiki/Web_scraping
  [5]: https://docs.scrapy.org/en/latest/intro/install.html
  [6]: https://docs.continuum.io/anaconda/
  [7]: https://docs.scrapy.org/en/latest/topics/commands.html

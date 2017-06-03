Python Website Crawler/Analyzer 
========================

> This project is used as an example that we build up in my book: [Learning Concurrency with Python](https://www.packtpub.com/application-development/learning-concurrency-python)

The PyCrawler is a multithreaded Python web crawler that utilizes BeautifulSoup and the urllib.request modules in order to crawl every page of a given website.

## Example

~~~python
> python3.6 main.py
> Website > https://tutorialedge.net
# Performs crawl
# Outputs to results.csv 
~~~ 

This crawler was built with the intention of being a teaching resource for my upcoming book `Learning Concurrency with Python`.  

## Features

* Crawls all links of a given web domain and checks to see response status code. 
* Performs all crawls using concurrent python practices
* Writes the results of each page crawl back to a results.csv file

## Todo

* Analyse each page to check to see if it complies with on-site SEO checklist

## On-Page Checklist

* Must contain a single `<title>` tag within the `<head>`
* Must contain `<meta name="description" content="...">`
* Images should contain `alt="keyword"` attribute
* Report back 5 most popular keywords on all pages
* Report back the size of each page and split this into buckets of js, css, images, other...
* Report back the number of requests each page take to load and categorize each into buckets
* Perform load time analysis of each page
* Report back if Javascript and CSS is not minified

Python Website Crawler/Analyzer 
========================

> This project is used as an example that we build up in my book: [Learning Concurrency with Python](https://www.packtpub.com/application-development/learning-concurrency-python)

## Features

* Crawls all links of a given web domain and checks to see response status code. 

## Todo

* Report back all of the links that give statuses other than 200. 
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

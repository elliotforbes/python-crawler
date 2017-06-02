import threading
import queue
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from crawler import *
import csv
from CheckableQueue import *

THREAD_COUNT = 20
linksToCrawl = CheckableQueue()

def run(url):
    try:
      result = Crawler.crawl(threading.current_thread(), url, linksToCrawl)
      linksToCrawl.task_done()
      return result
    except:
      raise Exception("Exception thrown with link: {}".format(url))


def appendToCSV(result):
  print("Appending result to CSV File: {}".format(result))
  with open('results.csv', 'a') as csvfile:
    resultwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    resultwriter.writerow(result)
    

def main():
  url = input("Website > ")
  Crawler(url)
  linksToCrawl.put(url)
  while not linksToCrawl.empty():
    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
      url = linksToCrawl.get()
      futures = []
      
      if url is not None:
        future = executor.submit(run, url)
        futures.append(future)

      for future in as_completed(futures):
        try:
          if future.result() != None:
            appendToCSV(future.result())  
        except:
          print(future.exception())

  print("Total Links Crawled: {}".format(len(Crawler.crawledLinks)))
  print("Total Errors: {}".format(len(Crawler.errorLinks)))

if __name__ == '__main__':
  main()
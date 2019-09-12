#Sequential scarpping of data from amazon and flipkart
import sys
sys.path.append("C:\Python\Lib\site-packages")
import requests
from bs4 import BeautifulSoup
import os
import time
import threading

def Flipkart_extraction(URL):
        flipkart_page = requests.get(URL, headers={"User-Agent": "Defined"})
        flipkart_soup = BeautifulSoup(flipkart_page.content, "html.parser")
        print("*******************************************FLIPKART********************************************************")
        print("ID of process running on Flipkart: {}".format(os.getpid()))
        print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
        print("\n")
        try:
            for item in flipkart_soup.findAll(class_="_2cLu-l"):
                item_nm = item.get_text()
                print("Flipkart Item Name: ", item_nm)
            for price in flipkart_soup.findAll(class_="_1vC4OE"):
                price = price.get_text()
                print("Flipkart Item Price: ",price)
            for rating in flipkart_soup.findAll(class_="hGSR34"):
                rating = rating.get_text()
                print("Flipkart Item Rating: ", rating," out of 5 stars")

        except AttributeError:
            print("Out of Scope")

def Amazon_extraction(URL):
    page = requests.get(URL, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    print("***********************************************AMAZON******************************************************")
    print("ID of process running on Amazon : {}".format(os.getpid()))
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("\n")
    try:
        for items in soup.findAll(class_="a-size-medium a-color-base a-text-normal"):
            item_name = items.get_text()
            print("Amazon Item Name: ", item_name)
        for price in soup.findAll(class_="a-price-whole"):
            price = price.get_text()
            print("Amazon Item Price: ", price)
        for rating in soup.findAll(class_="a-icon-alt"):
            rating = rating.get_text()
            print("Amazon Item Rating: ", rating)

    except AttributeError:
        print("Out of Scope")


if __name__ == "__main__":

    print("ID of main process: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))
    item = input("Enter the name of the item for which you want to compare the price: ")
    item = item.lower()
    item = item.split()
    item = ("-").join(item)
    #print(item)

    url1 = 'https://www.flipkart.com/search?q='
    url2 = 'https://www.amazon.in/s?k='
    url1 = url1 + item
    url2 = url2 + item

    print("Flipkart URL: ", url1)
    print("Amazon URL: ", url2)
    begin = time.time()
    Flipkart_extraction(url1)
    Amazon_extraction(url2)

    print("*******************FINISH**********************\n")
    print("Total time taken: ",begin - (time.time()))

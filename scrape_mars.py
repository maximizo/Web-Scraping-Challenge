
#Import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import os
import time
from webdriver_manager.chrome import ChromeDriverManager

#Set up chromedriver
def init_browser(): 
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    mars_dict = {}
    browser = init_browser()

#Visit html and set up beautifulsoup object
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'lxml')
    #print(soup)

#Extract news title and paragraph
    news_title = soup.find('div', class_='nav_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    print(f'Title: {news_title}')
    print(f'Paragaph: {news_p}')

#Extract image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    image_html = browser.html
    soup = bs(image_html, 'lxml')
    #print(soup)

    #Identify image url 
    image = soup.find_all('div', class_='img')[0].img['src']
    featured_image_url = f'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars{image}'
    print(featured_image_url)

    #Extract Mars facts
    facts_url = 'https://space-facts.com/mars/'
    facts_table = pd.read_html(facts_url)
    facts_table[0]

    #Convert table to html table string
    facts_table_html = facts_table[0].to_html()
    #print(facts_table_html)

    #Obtain Mars hemisphere images
    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)
    hem_html = browser.html
    #print(hem_html)

    hem_soup = bs(hem_html, "html.parser")
    #print(hem_soup)

    images = hem_soup.find_all('div',class_='item')
    hem_img_urls = []
    for image in images: 
        dict_ = {}
        titles = image.find('h3').text
        end_link = image.find('a')['href']
        image_link = 'https://astrogeology.usgs.gov/' + end_link
        browser.visit(image_link)
        html = browser.html
        soup = bs(html, 'html.parser')
        downloads = soup.find('div', class_='downloads')
        image_url = downloads.find('a')['href']
        print(titles)
        print(image_url)
        dict_['title'] = titles
        dict_['image_url'] = image_url
        hem_img_urls.append(dict_)

    #Add to dictionary
    mars_dict['news_title'] = news_title
    mars_dict['news_p'] = news_p
    mars_dict['featured_image_url'] = featured_image_url
    mars_dict['facts_table_html'] = facts_table_html
    mars_dict['hem_img_urls'] = hem_img_urls

    browser.quit()

    print(mars_dict)

    return mars_dict



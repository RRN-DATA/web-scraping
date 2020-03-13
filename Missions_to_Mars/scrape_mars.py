import pandas as pd
import matplotlib as plt
from bs4 import BeautifulSoup as bs
import requests
import splinter as sp
from bs4 import SoupStrainer as ss
from splinter import Browser
from bs4 import BeautifulSoup

from splinter import Browser
import os
import time
import datetime as dt


executable_path = {"executable_path": "/usr/local/Caskroom/chromedriver/80.0.3987.106/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

class LoadScrapeClass():
	def LoadSoup(url,secs):
		browser.visit(url)
		time.sleep(int(secs))
		html=browser.html
		soup = bs(html, "html.parser")
		return soup

	def LoadLatestMarsNews():
		url_to_nasa = "https://mars.nasa.gov/news/"
		soup = LoadScrapeClass.LoadSoup(url_to_nasa,10)
		news_title_list=[]
		

		newstitle=soup.find('div', class_='content_title').text
		newscontent=soup.find('div', class_='article_teaser_body').text
		
		news_title_dict = soup.find_all("div", class_='list_text')
		for title in news_title_dict:
			div_con=title.find_all('div', class_='content_title')
			#print(div_con)
			for tit in div_con:
				#print (tit.a.text)
				news_title_list.append(tit.a.text)
		
		news_para=[]
		news_para_list = soup.find_all("div", class_='article_teaser_body')
		for para in news_para_list:
			div_para=para.find_all("div", class_='article_teaser_body')
			#print(div_para)
			for tex in div_para:
				#print(tex.text)
				news_para.append(tex.text)
		news=[news_title_list,news_para]
		return newstitle,newscontent
		
	def LoadFeaturedImageURL():
		url_to_marsimg="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
		#browser.visit(url_to_marsimg)
		#image_html=browser.html
		#img_soup = bs(image_html, "html.parser")
		
		img_soup = LoadScrapeClass.LoadSoup(url_to_marsimg,2)
		imgurl=img_soup.find("img", class_="thumb")["src"]
		#startposition=imgurl.find("(",0,len(imgurl))+2
		#endposition=imgurl.find(")",0,len(imgurl))-1
		#imgurl=imgurl[startposition:endposition]
		featured_image_url = "https://www.jpl.nasa.gov" + imgurl

		return(featured_image_url)
	
	def LoadMarsWeather():
		twtr_url = 'https://twitter.com/marswxreport?lang=en'
		tsoup = LoadScrapeClass.LoadSoup(twtr_url,5)
		twtbody = tsoup.body.find_all('span')
 
		mars_weather=""
		for twt in twtbody: 
    			#print(twt.text)
			mars_weather_twt = twt.text
			if 'sol' and 'pressure' in mars_weather_twt:
				mars_weather=mars_weather_twt
				return(mars_weather)
				break
			else:
				pass
		return mars_weather

	def LoadMarsStatsTable():
                marsfacts_url="https://space-facts.com/mars"
                browser.visit(marsfacts_url)
                tables=pd.read_html(marsfacts_url)

                mars_data = pd.DataFrame(tables[0])
                mars_Stats = mars_data.to_html(header = False, index = False)
                return(mars_Stats)

	def scrapeImageURLs():
		marsimage="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
		#browser.visit(marsimage)

		#html = browser.html
		#mhsoup = bs(html, "html.parser")
		mhsoup = LoadScrapeClass.LoadSoup(marsimage,3)
		hemisphere_image_urls_list = []

		result = mhsoup.find("div", class_ = "result-list" )
		hemispheres = result.find_all("div", class_="item")
                        

		for hemi in hemispheres:
			title= hemi.h3.text.replace("Enhanced","")
			subpage="https://astrogeology.usgs.gov" + hemi.a["href"]
			browser2 = Browser("chrome", **executable_path, headless=False)

			browser2.visit(subpage)
			time.sleep(3)
			subhtml=browser2.html
			subsoup=bs(subhtml,"html5lib")
			loaddownloads=subsoup.find('div',class_='downloads')
			complete_img=loaddownloads.find("a")["href"]
			hemisphere_image_urls_list.append({"title":title,"img_url":complete_img})
			browser2.quit()
		return hemisphere_image_urls_list

	def scrape():
		mars_news = LoadScrapeClass.LoadLatestMarsNews()
		all_data = {
			'news_title' :  mars_news[0],
			'news_para' :  mars_news[1],
			'featured_image_url' : LoadScrapeClass.LoadFeaturedImageURL(),
			'mars_weather' : LoadScrapeClass.LoadMarsWeather(),
			'mars_facts' : LoadScrapeClass.LoadMarsStatsTable(),
			'hemisphere_image_urls' : LoadScrapeClass.scrapeImageURLs(),
			'timestamp' : dt.datetime.now()
			}
		browser.quit()
		return all_data

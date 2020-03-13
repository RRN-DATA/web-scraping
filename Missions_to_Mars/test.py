from scrape_mars import LoadScrapeClass
import pandas as pd

s=LoadScrapeClass.scrape()
class getNasaData():
	def getNasaTitle():
		title = s['news_title']
		return title
	def getNasaPara():
		para = s['news_para']
		return para
	def getFeaImage():
		fea_img = s['featured_image_url']
		return fea_img
	def getWeather():
		weather = s['mars_weather']
		return weather
	def getTable():
		table = s['mars_facts']
		return table
	def getDictUrls():
		dict_urls = s['hemisphere_image_urls']
		return dict_urls


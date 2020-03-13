import pymongo

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use

db = client.nasa_data
collection = db.mars_data
from scrape_mars import LoadScrapeClass

s=LoadScrapeClass.scrape()

db.collection.insert_many(
        [{'news_title': 'Mars Now'},
        {'news_para': 'NASA chose a seventh-grader from Virginia as winner of the agency\'s "Name the Rover" essay contest. Alexander Mather\'s entry for "Perseverance" was voted tops among 28,000 entries. '},
        {'featured_image_url': 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23745-640x350.jpg'},
        {'mars_weather': 'InSight sol 457 (2020-03-10) low -95.7ºC (-140.3ºF) high -9.1ºC (15.6ºF)\nwinds from the SSE at 6.5 m/s (14.5 mph) gusting to 21.0 m/s (46.9 mph)\npressure at 6.30 hPa'}, 
        {'mars_facts': '<table border="1" class="dataframe">\n  <tbody>\n    <tr>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <td>Surface Temperature:</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'},
        {'hemisphere_image_urls': [{'title': 'Cerberus Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere ', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}] }
        ])

print("Data Uploaded!")

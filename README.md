## Project Description
In this project, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Features & Libraries

* Python
* BeautifulSoup
* Pandas
* Requests/Splinter
* HTML
* MongoDB
* Flask
* OS
* Time
* ChromeDriver
* Pymongo

## My Process

1. Complete my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
2. Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of my scraping and analysis.
3. Scrape title & paragraph text:
  * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.
4. Scrape the feature image: 
  * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars), use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.
5. Scrape facts about the planet: 
  * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
6. Use Pandas to convert the data to an HTML table string.
7. Scrape high-res hemisphere images: 
  * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
  * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Store the data using keys. 
  * Append the dictionary with the image url string and the hemisphere title to a list. 
8. Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped.
9. Convert Jupyter notebook into a Python script. Include a function called `scrape` that will execute the scraping code from above and return one Python dictionary containing all of the scraped data.
10. Create a route that will import my script and call the `scrape` function.
11. Store the return values in Mongo as a Python dictionary.
12. Create a root route that will query the Mongo database and pass the mars data into an HTML template.
13. Create a template HTML file called that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

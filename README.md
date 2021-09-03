
# Prerequisites

install using `requirements.txt`

1)To install scrapy : `pip3 install scrapy` 
2)To install testmaster : ` pip3 install scrapy-testmaster`

# Architecture of Application

There are 4 main steps.

## Step 1:
Run `scrapy startproject <project name>` . Move to project directory
I built first spider `company_index.py` which crawls the website `https://www.adapt.io/directory/industry/telecommunications/A-1`. There are a list of companies mentioned in the website. I had to scrape the company name and source url enclosed within, by deriving the xpath.
To run the spider we have to run `scrapy crawl company -o company_index.json` which will save the output in a json file

## Step 2:
I built the second spider which opens `https://www.adapt.io/directory/industry/telecommunications/A-1`, crawls through each company in the list , follows the link 
using `callback` method.
To run the spider we have to run `scrapy crawl profiles -o company_profiles.json`
scrapes the data each url as per requirement.

## Step 3:
Used mongodb compass for loading json data into database.

port =  `localhost:27017`

Made a separate foder : `databases` to write code to import json data to mongodb.

Also copied the json files to the same folder

## Step 4:
Built test cases with `scrapy-testmaker`.

#### Setup:
Install scrapy-testmaker. 
Go to `settings.py` file, set `SPIDER_MIDDLEWARES = {
    'scrapy_testmaster.TestMasterMiddleware': 950
}` & `TESTMASTER_ENABLED = True`



# Reason I used mongodb:
I could easily load the data into database by importing the json file




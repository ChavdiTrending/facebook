# facebook Server side scripts for fetching trending affairs and news
Server Side facebook scripts
This repository contain all the server side scripting for fetching all the trending data from facebook,
Currently the trending section of facebook is built up by rss feeds from over 1000 news websites, running the deserializeJson.json file will make a json file which will have title and links of all the trending news.
To run this script do the following steps:

Dependency-
pip install -e git+https://github.com/alex-sherman/deco.git#egg=deco
pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

1.To re-fetch Facebook's PDF and re-parse it into data/rss-urls.csv:

**python scripts/fetch_pdf.py** 

2.The following script will run through each entry in data/rss-urls.csv to fetch each RSS URL and save the response to a corresponding JSON file in data/feeds/:

**python scripts/fetch_feeds.py**

3.To create Json file having all the links and description run this command

**python deserializeJson.py**

This will give you a file named deserializeJson.json which has all the link along with it's title

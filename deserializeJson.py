import json
import xmltodict
import os
'''
with open('deadline.com---feed.json') as json_data:
    d = json.load(json_data)
    print(d)
'''
listofallthejsonfile = os.listdir('data/feeds')
jsonDict = {}
for string in listofallthejsonfile:
	print(string)
	try:
		print('in')
		stringfin = 'data/feeds/'+string
		jdata = json.load(open(stringfin))
		feed = xmltodict.parse(jdata['response_text'])
		print(feed['rss']['channel']['title'])
		jsonDict[feed['rss']['channel']['title']] = [] #list for json title and links
		# Deadline
		items = feed['rss']['channel']['item']
		len(items)
		print(len(items))
		for i in range(len(items)):
			# 12
			jsonDict[feed['rss']['channel']['title']].append({
				'title':items[i]['title'],
				'link':items[i]['link']
				})
			print(items[i]['title']) 
			# The CW Looking To Redevelop Kevin Williamson Paranormal Drama
			print(items[i]['link'])
	except:
		print('Error in json file')
with open('links.json', 'w') as outfile:  
    json.dump(jsonDict, outfile)



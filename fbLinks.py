#App Access token :- 679028202487209|abdfSPAaQclXA9JRYBQ5ZIXZccY
#The following API if hit will give you link of all the posts of current year
import facebook
import datetime
import requests
import json

graph = facebook.GraphAPI(access_token="679028202487209|abdfSPAaQclXA9JRYBQ5ZIXZccY", version="2.11") #this access token if of our app
post = graph.get_object(id='realmadrid/posts', fields='link,created_time')
#print(post['data'][0]['created_time'][:10])
#print(len(post['data']))
#post = requests.get(post['paging']['next']).json()
#print(post)

links = []
now = datetime.datetime.now()
date  = "".join([str(now.year),"-",str(now.month),"-",str(now.day)])
while(True):
	try:
		count = len(post['data'])
		for i in range(count):
			if(post['data'][i]['created_time'][:4] == str(now.year)):
				links.append(post['data'][i]['link'])
			else:
				break		
		if (i == count-1 and post['paging']):
			post=requests.get(post['paging']['next']).json()
		else:
			break
	except:
		print(links)
		break;
print(links)
print(len(links))
jsonDict = {}
jsonDict['links'] = links
with open('Postlinks.json', 'w') as outfile:  
    json.dump(jsonDict, outfile)

#!/usr/bin/python2
import webbrowser,requests,platform,commands,os
#BeautifulSoup for web scrapping
from bs4 import BeautifulSoup
menu='''
	Press 1:To search each word of the message in new tab
	Press 2:To search images of each word of the message in new tab 
	Press 3:To print url of first page of google search of the message
	Press 4:To print current date and time
	Press 5:To open default webbrowser after detecting the OS
	Press 6:To print all IPs of the network
	Press 7:To print the details of the owner of any domain name 
'''
print menu
ch=raw_input("Enter your choice")
if ch=='1':
	search_data=raw_input("Enter a message")
#strip() removes extra spaces in search_data
	strip_data=search_data.strip()
#split() separates each word of strip_data
	single_word=strip_data.split()
	for i in single_word:
#webbrowser.open_new_tab() opens a new tab for searching of each 'i'
                webbrowser.open_new_tab("https://www.google.com/search?q="+i)
elif ch=='2':
	search_data=raw_input("Enter a message")
        strip_data=search_data.strip()
        single_word=strip_data.split()
	for i in single_word:
		webbrowser.open_new_tab("https://www.google.com/images?q="+i)
elif ch=='3':
	search_data=raw_input("Enter a message")
#requests.get (url) requests to get the webpage whose url is mentioned in paranthesis 
        r=requests.get("https://www.google.com/search?q="+search_data)
#converts the url into text
	data=r.text
#BeautifulSoup parses the data
	soup=BeautifulSoup(data)
#to get all the links
	all_links=soup.find_all("a")
	for link in all_links:
		url=link.get("href")
		domain=url.split("://")[-1].split("/")[0]
		domain.strip()
    		print domain
elif ch=='4':

	print "Current time and date" 
	time.ctime()
elif ch=='5':
	op=platform.system() #to know the current os
	if op=="Linux":
		webbrowser.get("firefox").open("https://www.google.com")
	        
elif ch=='6':
	print ""
elif ch=='7':
	print ""
else:
	print "Invalid choice!!"

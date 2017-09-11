#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import urllib
from time import *
import os
#from BeautifulSoup import *
#from pyvirtualdisplay import Display

#display = Display(visible=0, size=(800, 600))
#display.start()

wordimg=input("dowload google big image search  for : \n")
print ("searching about img about :",wordimg,".......")
url = 'https://www.google.com/search?' + urllib.urlencode({'site':'imghp',
'q': wordimg , 'oq':wordimg , 'source':'lnms','tbm':'isch','newwindow':'1','hl':'en','source':'hp','tbs':'islt:svga,isz:l'})

print ("retriving URL : ",url,"......")


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.add_extension('quickjava-2.1.0-fx.xpi')
firefox_profile.set_preference('thatoneguydotnet.QuickJava.curVersion', '2.1.0') ## Prevents loading the 'thank you for installing screen'
firefox_profile.set_preference('thatoneguydotnet.QuickJava.startupStatus.Images', 2) ## Turns images off
firefox_profile.set_preference('thatoneguydotnet.QuickJava.startupStatus.AnimatedImage', 2) ## Turns animated images off

firefox_profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.CSS", 2)  ## CSS
#firefox_profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Cookies", 2)  ## Cookies
firefox_profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Flash", 2)  ## Flash
firefox_profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Java", 2)  ## Java
#firefox_profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.JavaScript", 2)  ## JavaScript
firefox_profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Silverlight", 2) 

#binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\firefox.exe")


driver = webdriver.Firefox(executable_path=r'\geckodriver.exe',firefox_profile=firefox_profile)

driver.get(url)


print ("===============\n")

hr = driver.page_source
driver.close()
print ("len of hr: ",len(hr))
hrsp = hr.split('<div class="rg_meta">')
print ("len of splits",len(hrsp))
imgurlsn=list()
com='0'
for iii in hrsp:
	imgurl=re.findall('.+"ou":"(.+jpg)".*',iii)
	if len(imgurl)>0:
		imgurlsn.append(imgurl[0])
		print (imgurl)
		com='wget -c --read-timeout=5 --tries=0 -P '+wordimg+' '+imgurl[0]
		os.system(com)
'''
so=BeautifulSoup(hr)
tags0=so("a")
print "len of tag('a') : ", len(tags0)
urls=list()

for ic in tags0 :
	if (ic.get('href', None) != None) & (ic.get('class',None)=='rg_l') :
		urls.append('https://www.google.com'+ic.get('href', None))

print "len of urls is : ",len(urls)
print "================\n"

driver.get(urls[2])

driver.get('https://www.google.com/imgres?imgurl=http%3A%2F%2Fep.yimg.com%2Fay%2Fyhst-17210252890263%2Fsyma-x5sc-explorers-4-channel-6-axis-rc-quadcopter-drone-ready-to-fly-2-4ghz-w-hd-camera-4gb-memory-card-black-1.jpg&imgrefurl=http%3A%2F%2Fwww.nitroplanes.com%2Fquadcopters.html&docid=ParMNGR3khQG_M&tbnid=ty19N4PAXqYWfM%3A&w=285&h=163&hl=en&bih=481&biw=1024&ved=0ahUKEwianbqVr8nPAhVsJJoKHfNoDAEQMwggKAIwAg&iact=mrc&uact=8')
#xpath_of_icon = '//*[@id="rg_s"]/div['+28+']/a/img'
#ele=driver.find_element_by_xpath('//*[@id="rg_s"]/div[89]/a')

print "retriving new single icon......"

hr = driver.page_source
hrb=BeautifulSoup(hr)
f=hrb("a")
viewim=f[0]
for ii in f :
	print ii
	m=re.findall('^<a class="irc_fsl irc_but i3596".+',str(ii))
	if len(m)==0 :
		print "!!!!!!! continue !!!!!!!!!\n"
		continue
	viewim=ii
fs=viewim.get_attribute("data-href")
print fs

#ele=driver.find_element_by_xpath('//*[@id="irc_cc"]/div[2]/div[3]/div[1]/div[2]/table[1]/tbody/tr/td[2]/a')
#url=ele.get_attribute("href")

url=driver.title[24:]
print "url is ",url
com='wget -c --read-timeout=5 --tries=1 -P "nw" '+url
os.system(com)
print driver.title'''
print (len(imgurlsn))

#display.stop()




########################################################################
"""
import urllib2

attempts = 0

while attempts < 3:
    try:
        response = urllib2.urlopen("http://example.com", timeout = 5)
        content = response.read()
        f = open( "local/index.html", 'w' )
        f.write( content )
        f.close()
        break
    except urllib2.URLError as e:
        attempts += 1
        print type(e)
"""
#wget -c --read-timeout=5 --tries=0 "$URL"

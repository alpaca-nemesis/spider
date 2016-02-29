#coding=utf-8
import urllib

def getHtml(url):
	page = urllib.open(url)
	html = page.read()
	return html

html = getHtml("http://www.dota2shop.cn/?")

print html
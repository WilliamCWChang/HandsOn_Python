import requests
import shutil
from bs4 import BeautifulSoup
# import Image
import os




link = {
"來自深淵/001集": "10705332" ,
"來自深淵/002集": "10705368" ,
"來自深淵/003集": "10705388" ,
"來自深淵/004集": "10705402" ,
"來自深淵/005集": "11681742" ,
"來自深淵/006集": "11681765" ,
"來自深淵/007集": "11681776" ,
"來自深淵/008集": "11681797" ,
"來自深淵/009集": "11805646" ,
"來自深淵/010集": "12049050" ,
"來自深淵/011集": "12049089" ,
"來自深淵/012集": "12173265" ,
"來自深淵/013集": "12303462" ,
"來自深淵/014集": "12317964" ,
"來自深淵/015集": "12422775" ,
"來自深淵/016集": "12509378" ,
"來自深淵/017集": "12869464" ,
"來自深淵/018集": "13238763" ,
"來自深淵/019集": "13310559" ,
"來自深淵/020集": "13395674" ,
"來自深淵/021集": "13429253" ,
"來自深淵/022集": "13473282" ,
"來自深淵/023集": "13506330" ,
"來自深淵/024集": "13506352" ,
"來自深淵/025集": "13586401" ,
"來自深淵/026集": "13609539" ,
"來自深淵/027集": "13619781" ,
"來自深淵/028集": "13642029" ,
"來自深淵/029集": "13642046" ,
"來自深淵/030集": "13656846" ,
"來自深淵/031集": "13656872" ,
"來自深淵/032集": "13662028" ,
"來自深淵/033集": "13662061" ,
"來自深淵/034集": "13691934" ,
"來自深淵/番外篇01": "12173257" ,
"來自深淵/番外篇02": "12840375" ,
"來自深淵/番外篇03": "13570840" }





def get_commic(dir_name, link_name):
	for page in range(1,200):
		html_doc = requests.get('http://comic.ck101.com/vols/' + link_name + '/' + str(page) + '/1')
		print(html_doc)
		soup = BeautifulSoup(html_doc.text, 'html.parser')
		img = soup.find(id="comicPic")
		print(img)
		if img is None:
			break
		img_url = img.attrs['src']
		print(img_url)
		r = requests.get(img_url, stream=True)
		print(r)
		response = requests.get(img_url, stream=True)
		# dir_name = "111/"
		if not os.path.exists(dir_name):    #先確認資料夾是否存在
			os.makedirs(dir_name)
		handle = open(dir_name + "/" + str(page) + ".jpg", "wb")
		for chunk in response.iter_content(chunk_size=512):
		    if chunk:  # filter out keep-alive new chunks
		        handle.write(chunk)

for i in link:
	get_commic(i, link[i])
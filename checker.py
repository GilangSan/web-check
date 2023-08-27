import os
import requests
from bs4 import BeautifulSoup

def ipcheck(url):
  os.system("clear")
  page = requests.get("https://check-host.net/ip-info?host="+url)
  soup = BeautifulSoup(page.text, 'html.parser')
  my = soup.findAll('strong')[1]
  mys = soup.find('td').findAll('td')[4]
  host = mys.get_text()
  ip = my.get_text()
  txt = "Data Ditemukan!\nIp : "+ip+"\nHostName : "+host
  print(txt)
  input("Enter To Back")

def source(url):
  os.system("clear")
  page = requests.get(url)
  soup = BeautifulSoup(page.text)
  print(soup)
  input("Enter To Back")

def findd(url):
  os.system("clear")
  apa = input("Masukkan Element ( Contoh h1, p, button ) ")
  page = requests.get("https://check-host.net/ip-info?host="+url)
  soup = BeautifulSoup(page.text, 'html.parser')
  ayak = soup.findAll(apa)
  print(ayak)
  input("Enter To Back")

def tools(url):
  os.system("clear")
  print("Pilih Tools Dibawah\n1) Ip Checker ( Check Ip )\n2) Source HTML ( Source Code Web )\n3) Class Finder ( Pencari Element )")
  sel = int(input("Nomor : "))
  if sel == 1:
    ipcheck(url)
  if sel == 2:
    source(url)
  if sel == 3:
    findd(url)
  else:
    tools(url)

while True:
  os.system("clear")
  print("Masukkan url yang ingin di check dibawah")
  url= input("Url : ")
  tools(url)

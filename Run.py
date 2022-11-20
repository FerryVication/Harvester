# -*- coding: UTF-8 -*-
# ToolName   : EmailScrapper
# Author     : FeriPratama
# Version    : 1.0 ( beta }
# License    : MIT
# Copyright  : FeriPratama (2022-2023)
# Github     : https://github.com/CyberCarboon2
# Contact    : https://www.facebook.com/smart.danie.3
# Description: EmailScrapper is a tool for scraping email from Website
# Tags       : Scrapper,Email
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Happy Hacking !!!
"""
MIT License

Copyright (c) 2022 FeriPratama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os,sys,time
try:
  import requests
except ImportError:
  os.system('pip install -r requirements.txt')
from collections import deque
from bs4 import BeautifulSoup
#import deque
b = '\033[34;1m' #biru
h = '\033[32;1m' #hijau
u = '\033[35;1m' #ungu
bm = '\033[36;1m' #biru muda
red = '\033[31;1m' #merah
p = '\033[37;1m' #putih
k = '\033[33;1m' #kuning
import urllib.parse
import re
os.system('clear')

print(f'''
 {b}_____ __  __    _    ___ _       ____   ____ ____      _    ____  _____ ____
{u}| ____|  \/  |  / \  |_ _| |     / ___| / ___|  _ \    / \  |  _ \| ____|  _ \       Code By :
{bm}|  _| | |\/| | / _ \  | || |     \___ \| |   | |_) |  / _ \ | |_) |  _| | |_) |     Feri-DP
{k}| |___| |  | |/ ___ \ | || |___   ___) | |___|  _ <  / ___ \|  __/| |___|  _ <       Version :
{b}|_____|_|  |_/_/   \_\___|_____| |____/ \____|_| \_\/_/   \_\_|   |_____|_| \_\      1.0 ( beta )
{h}------------------------------------------------------------------------------->

''')
print('[+] Masukkan Link Website Yang Akan Di Scrape Email Nya contoh https://www.contoh.com/')
user_url = str(input('[+] Masukkan Link : '))
limit = int(input('[+] Masukkan Limit : '))
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0

try:
  while True:
    count += 1
    if count > limit:
      break
    url = urls.popleft()
    scraped_urls.add(url)
    parts = urllib.parse.urlsplit(url)
    base_url = f'{parts.scheme}://{parts.netloc}'
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    print(f'[ {count} ] Memproses {url}')
    
    try:
      response = requests.get(url)
    except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
      print('[!] Mohon Maaf Terdapat Kesalahan Yang Tidak Diketahui !!!')
      os.system('exit')
    new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.+[a-z\.]+', response.text, re.I))
    emails.update(new_emails)
    soup = BeautifulSoup(response.text, 'html.parser')
    for anchor in soup.find_all('a'):
      link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
      if link.startswith('/'):
        link = base_url + link
      elif not link.startswith('http'):
        link = path = link

      if not link in urls and not link in scraped_urls:
        urls.append(link)
except KeyboardInterrupt:
  print('[-] Closing !')
  
print('\n Proses Selesai !')
print(f'{len(emails)} Email Ditemukan \n =============')

for mail in emails:
  print(' '+mail)

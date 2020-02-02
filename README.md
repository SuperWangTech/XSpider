# Welcome to my project

## Description  
Django embeds a "spider" script, grabs Douban top250 movie information, 
saves it to a mysql database, and displays data analysis on the command line or web page.

## Usage  

```bash
git clone git@github.com:SuperWangTech/XSpider.git
cd XSpider

# setup env
pipenv install

# write your db config
vim xspider/settings_local.py

# try spider
python manage.py spider -s douban -o *.html
```

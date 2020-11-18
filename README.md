# properti-scrapy

## Python web crawling using scrapy

This repository created to crawl Indonesia property (especially house) feature and price.

### FIRST SETUP
```
git clone https://github.com/yosepalexsander/properti-scrapy.git
pip install -r requirements.txt
or
poetry update
```

### RUNNING SCRIPT
```
cd rumah_scrapper
```
```
scrapy crawl -a iklan=(jual or sewa) -a properti=rumah -a max_page=5000 (default=1000)
```

### ATTENTION
if you face literals error in your spider, just ignore it because the value is not relevant with the item keys  
i.e : expected value is 52 but got 52² (contain unicode)

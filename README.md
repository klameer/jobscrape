# Consolidate job postings from various job sites

The Python libraries this needs to run are:

Flask
Requests
BeautifulSoup
TinyDB

## Installation
To get up and running
```
git clone https://github.com/klameer/jobscrape.git
cd jobscrape

pip install flask requests bs4 tinydb
python scrape.py # creates a database of jobs
python serve.py # displays the jobs in a table

```

When ```serve.py``` is running, go to ```http://127.0.0.1:8000``` on your browser.

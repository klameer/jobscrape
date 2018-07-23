import requests
import bs4 as bs
import re
import datetime

from tinydb import TinyDB

today = datetime.datetime.now().strftime("%Y-%m-%d")

def get_monster():
    url = 'https://www.monster.co.uk/jobs/search/Contract_8?q=Data-Analyst&where=london&sort=dt.rv.di'

    final = []
    resp = requests.get(url)
    soup = bs.BeautifulSoup(resp.text, "lxml")

    jobs = soup.find("section", {"id":"resultsWrapper"}).find_all("article", {"class":"js_result_row"})

    for job in jobs:
        job_title = job.find("div", {"class":"jobTitle"}).find("a").text
        job_link = job.find("div", {"class":"jobTitle"}).find("a").get("href")
        job_title = re.sub("\n|\r", "", job_title)

        job_date = job.find("time").get("datetime")
        job_date = datetime.datetime.strptime(job_date, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d")

        row = {"source":"monster", "title": job_title, "link": job_link, "time":job_date}

        if job_date == today:
            final.append(row)

    return final

def get_total_jobs():
    url = "https://www.totaljobs.com/jobs/contract/data"
    resp = requests.get(url)

    soup = bs.BeautifulSoup(resp.text, "lxml")
    jobs = []
    results  = soup.find_all("div", {"class":"job-title"})
    for result in results:
        job_title = result.find("a").text
        job_title = re.sub("\n", "", job_title)
        job_link = result.find("a").get("href")
        job = {"source":"totaljobs", "title":job_title, "link":job_link}
        jobs.append(job)

    results  = soup.find_all("div", {"class":"detail-body"})
    i = 0
    for result in results:
        job_date = result.find("li", {"class", "date-posted"}).text
        job_date = re.sub(" +|\n", "", job_date)
        jobs[i]["time"] = job_date
        i += 1
    final = []
    for job in jobs:
        if job['time'] == 'Today':
            final.append(job)

    return final

def write_db():
    db = TinyDB("myfile.json")
    db.purge()

    for job in get_monster():
        db.insert(job)

    for job in get_total_jobs():
        db.insert(job)

if __name__ == "__main__":
    write_db()
    

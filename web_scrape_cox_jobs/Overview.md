# Web Scraping Cox Enterprises Job Website
***
***
# Important notes:
* The script is relativly slow. It loads the site and its dynamic JS content, and then scans the page for the specific HTML elements.
* I have only tested this on Windows. There might be issues on other platforms due to the chrome driver it uses.


# What is this:
* This is a script that can be used to webscrape the Cox Enterprises job search results site: https://jobs.coxenterprises.com/job-search-results/
* There are dozens of jobs availible on the site, however the site only shows 10 per page. This script scans the pages you specify, grabs the job title and url and then outputs that data to an excel file.
# How to use this:
* create an instance of the class:
```
Jobs = JobScraper()
```
* use the .run() method to gather the data
* run (filename, base_url)
* the base url should be grabbed from the first page of the search results and should not contain "&pg=" at the end
```
my_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=lead%20security&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
    Jobs.run('job_details.xlsx', my_url)
```

### Run the script:
```
python web_scrape_cox_jobs.py
```
* The script opens a web browser and starts scanning the pages for the specific html/css elements
* Once the script completes it closes the browser 
* you should see a console output like this:
```
Collected 10 results from page 1
Collected 10 results from page 2
Collected 10 results from page 3
Collected 10 results from page 4
Collected 3 results from page 5
Gathered jobs from 5 pages
         Adding data to a new excel document
         You can see the job results in this file: - job_details.xlsx
```
* The excel file will be outputed to the same directory that the script is in

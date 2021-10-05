# Web Scraping Cox Enterprises Job Website
***
***

# What is this:
* This is a script that can be used to webscrape the Cox Enterprises job search results site: https://jobs.coxenterprises.com/job-search-results/
* There are dozens of jobs availible on the site, however the site only shows 10 per page. This script scans the pages you specify, grabs the job title and url and then outputs that data to a CSV file.
# How to use this:
### URL
* The specific search URL is specified in the script: 
```
search_query = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25&pg=" + str(page)
```
### Specify values
* Once you create the class object you have to specify the following:
* a) how many pages to scan
* b) the filename you want to use for the CSV file
```
Jobs.run(3,'job_details.csv')
```
### Run the script:
```
python web_scrape_cox_jobs.py
```
* The CSV file will be outputed to the same directory that the script is in
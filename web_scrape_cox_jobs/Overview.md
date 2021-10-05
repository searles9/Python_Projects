# Web Scraping Cox Enterprises Job Website
***
***
# Important notes:
* The script is relativly slow. It loads the site and its dynamic JS content, and then scans the page for the specific HTML elements.


# What is this:
* This is a script that can be used to webscrape the Cox Enterprises job search results site: https://jobs.coxenterprises.com/job-search-results/
* There are dozens of jobs availible on the site, however the site only shows 10 per page. This script scans the pages you specify, grabs the job title and url and then outputs that data to a CSV file.
# How to use this:
### Specify values
* Once you create the class object you have to specify the following:
* a) how many pages to scan
* b) the filename you want to use for the CSV file
* c) specify the base URL. The base url should not contain "pg=" at the end. The base url is generally page 1 of the search results.
```
the_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
Jobs.run(42,'job_details.csv', the_url)
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
```
* The CSV file will be outputed to the same directory that the script is in

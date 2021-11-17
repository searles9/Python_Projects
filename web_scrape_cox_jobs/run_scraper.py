import web_scrape_cox_jobs
import filter_jobs

# Need to add : a way to prevent having to recode the common bad terms (list comprehension)
# a way to auto capitalize all the terms in the lists (lowercase - then capitalize)

def securityJobs(oldfilename,newfilename):
    # Security Jobs
    good_terms = ["Security","Cyber"]
    bad_terms = ["Senior","Lead","Azure","Principal","Release","Sr","Software",
                 "Manager", "Financal","Finance","Payroll","HR","Marketing","SEO",
                 "Tax","Photojournalist","Executive","Sales","Buissness","Compensation","Recruiting",
                 "Litigation","Payable","Vehicle","Arbitrator","UX","Recruiter"]
    filter_jobs.filterexcel(oldfilename,newfilename,good_terms,bad_terms)

def generalFilteredJobs(oldfilename,newfilename):
    # Security Jobs
    good_terms = ["Security","Solutions","Cloud","Cyber","Reliability","Architect","Systems","System","Infrastructure"]
    bad_terms = ["Senior","Lead","Azure","Principal","Release","Sr","Software",
                 "Manager", "Financal","Finance","Payroll","HR","Marketing","SEO",
                 "Tax","Photojournalist","Executive","Sales","Buissness","Compensation","Recruiting",
                 "Litigation","Payable","Vehicle","Arbitrator","UX","Recruiter"]
    filter_jobs.filterexcel(oldfilename,newfilename,good_terms,bad_terms)

if __name__ == "__main__":
    # Get all the jobs and store them in 'job_details.xlsx'
    full_job_list = 'job_details.xlsx'
    # All full time, individual contributor roles
    site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
    Jobs = web_scrape_cox_jobs.JobScraper()
    Jobs.run(full_job_list,site_url)
    # Filter the original list and store the results in new excel files
    securityJobs(full_job_list,'security_jobs.xlsx')
    generalFilteredJobs(full_job_list,'general_filtered_jobs.xlsx')
    
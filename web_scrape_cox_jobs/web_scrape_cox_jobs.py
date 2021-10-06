from selenium import webdriver
import chromedriver_binary
import time
import pandas as pd


class JobScraper():
    job_details = []
    
    def get_jobs(self,base_url):
        page_still_valid = True
        page = 1
        driver = webdriver.Chrome()
        while page_still_valid:
            search_query = str(base_url) + "&pg=" + str(page)
            driver.get(search_query)
            time.sleep(5)
            job_list = driver.find_elements_by_class_name('job-innerwrap')
            if len(job_list) > 0:
                print(f"Collected {len(job_list)} results from page {str(page)}")
                for each_job in job_list:
                # Getting job info
                    job_title = each_job.find_elements_by_xpath(".//div[@class='jobTitle']")[0]
                    job_location = each_job.find_elements_by_xpath(".//div[@class='parent location']")[0]
                    job_division = each_job.find_element_by_xpath(".//li[@class='job-data business_unit']")
                    job_url = each_job.find_element_by_xpath(".//div[@class='jobTitle']/a").get_attribute('href')
                    # Saving job info 
                    job_info = [job_title.text, job_location.text, job_division.text, job_url]
                    # Saving into job_details
                    self.job_details.append(job_info)
            else: 
                print(f"Gathered jobs from {(page - 1)} pages")
                break
            page += 1
        driver.quit()

    def to_csv(self,filename):
        print(f"\t Adding data to a new CSV document")
        job_details_df = pd.DataFrame(self.job_details)
        job_details_df.columns = ['title', 'location', 'division', 'url']
        job_details_df.to_csv(filename, index=False)
        print(f"\t You can see the job results in this file: - {filename}")

    def run(self,filename,base_url):
        jobs = self.get_jobs(base_url)
        self.to_csv(filename)
        pass

if __name__ == "__main__":
    Jobs = JobScraper()
    my_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=lead%20security&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
    Jobs.run('job_details.csv', my_url)
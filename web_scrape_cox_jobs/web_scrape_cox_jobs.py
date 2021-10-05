from selenium import webdriver
import chromedriver_binary
import time
import pandas as pd


class JobScraper():
    job_details = []
    
    def get_jobs(self,pages):
        driver = webdriver.Chrome()
        for page in range(1,pages,1):
            search_query = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25&pg=" + str(page)
            driver.get(search_query)
            time.sleep(5)
            job_list = driver.find_elements_by_class_name('job-innerwrap')
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
        driver.quit()

    def to_csv(self,filename):
        print(f"\t Adding data to a new CSV document - {filename}")
        job_details_df = pd.DataFrame(self.job_details)
        job_details_df.columns = ['title', 'location', 'division', 'url']
        job_details_df.to_csv(filename, index=False)

    def run(self,pages,filename):
        jobs = self.get_jobs(pages)
        self.to_csv(filename)

if __name__ == "__main__":
    Jobs = JobScraper()
    Jobs.run(42,'job_details.csv')
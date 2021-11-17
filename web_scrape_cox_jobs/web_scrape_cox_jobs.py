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
                print(f"***Gathered jobs from {(page - 1)} pages")
                break
            page += 1
        driver.quit()

    def to_excel(self,filename):
        print("***Adding data to a new excel document")
        df = pd.DataFrame(self.job_details)
        df.columns = ['title', 'location', 'division', 'url']
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='All-Jobs', index=False)
        writer.save()
        print(f"***You can see the job results in this file: - {filename}")

    def run(self,filename,base_url):
        jobs = self.get_jobs(base_url)
        self.to_excel(filename)

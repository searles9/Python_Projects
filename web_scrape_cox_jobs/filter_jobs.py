import web_scrape_cox_jobs
import pandas as pd

def filterexcel(oldfilename,newfilename,good_terms,bad_terms):
    excel_file = oldfilename
    jobsdf = pd.read_excel(excel_file)
    # Filter data frame to once include show job titles that contain terms included in the good terms list
    if len(good_terms) > 0:
        jobsdf = jobsdf[jobsdf["title"].str.contains('|'.join(good_terms))]
    else:
        pass
    # Drop rows for job titles that contain terms in the bad terms list
    if len(bad_terms) > 0:
        jobsdf = jobsdf[jobsdf["title"].str.contains('|'.join(bad_terms))==False]
    else:
        pass
    writer = pd.ExcelWriter(newfilename, engine='xlsxwriter')
    jobsdf.to_excel(writer, index=False, sheet_name='Filtered-Jobs')
    writer.save()
    print(f"***{oldfilename} has been filtered to {newfilename}")



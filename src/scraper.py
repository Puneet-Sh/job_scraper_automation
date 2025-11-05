from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_jobs(keyword, location):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.indeed.com")

    time.sleep(3)
    driver.find_element(By.ID, "text-input-what").send_keys(keyword)
    driver.find_element(By.ID, "text-input-where").clear()
    driver.find_element(By.ID, "text-input-where").send_keys(location)
    driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton").click()
    time.sleep(5)

    job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
    jobs = []
    for job in job_cards[:20]:
        try:
            title = job.find_element(By.CSS_SELECTOR, "h2.jobTitle").text
            company = job.find_element(By.CLASS_NAME, "companyName").text
            location = job.find_element(By.CLASS_NAME, "companyLocation").text
            summary = job.find_element(By.CLASS_NAME, "job-snippet").text
            jobs.append({"Title": title, "Company": company, "Location": location, "Summary": summary})
        except:
            pass

    driver.quit()
    return jobs

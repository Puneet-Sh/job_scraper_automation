import json, logging, schedule, time
from scraper import scrape_jobs
from data_cleaner import clean_and_save
from reporter import send_email_report

logging.basicConfig(filename="logs/scraper.log", level=logging.INFO)

def run_pipeline():
    try:
        with open("config/config.json") as f:
            config = json.load(f)

        logging.info("Starting job scraping pipeline...")
        jobs = scrape_jobs(config["job_keyword"], config["location"])
        report_path = clean_and_save(jobs)
        send_email_report(config["email_sender"], config["email_password"], config["email_receiver"], report_path)
        logging.info("Pipeline completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

# Run daily at 10 AM
schedule.every().day.at("10:00").do(run_pipeline)

if __name__ == "__main__":
    run_pipeline()  # Run immediately for testing
    while True:
        schedule.run_pending()
        time.sleep(60)

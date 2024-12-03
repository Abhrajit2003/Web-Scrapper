import schedule
import time
from controller import insert_news  # Assuming the insert_news function is in controller.py
from scrapper import Scrapper

def show_data():
    sc = Scrapper()
    news = sc.scrapper()

    for index, n in enumerate(news):
        res = insert_news(
            heading=n.get('heading'),
            date=n.get('date'),
            news=n.get('news')
        )
        print(f"Data inserted: {index+1} | {res}")

# Schedule the task to run at 12:28 a.m. every day
schedule.every().day.at("12:33").do(show_data)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute

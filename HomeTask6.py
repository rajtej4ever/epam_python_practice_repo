import os
import datetime

class NewsFeed:
    def __init__(self):
        self.news_feed_file = "news_feed.txt"

    def add_news(self, text, city, current_date):
        record = f"NEWS|{text}|{city}|{current_date}\n"
        self._append_to_file(record)

    def add_private_ad(self, text, expiration_date, current_date):
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        days_left = (expiration_date - current_date).days
        record = f"PRIVATE_AD|{text}|{expiration_date}|{days_left} days left\n"
        self._append_to_file(record)

    def _append_to_file(self, record):
        with open(self.news_feed_file, "a") as file:
            file.write(record)


class NewsFeedProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.news_feed = NewsFeed()

    def process_records(self):
        current_date = datetime.datetime.now()
        processed_records = set()  # Set to store processed records

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                records = file.readlines()

            for record in records:
                parts = record.strip().split("|")
                record_type = parts[0]
                data = parts[1:]

                if record_type.lower() == "news" and len(data) == 3:
                    text, city, _ = data
                    processed_records.add((record_type, text, city))  # Add unique news record
                elif record_type.lower() == "private_ad" and len(data) == 2:
                    text, expiration_date = data
                    processed_records.add((record_type, text, expiration_date))  # Add unique private ad record

            for record in processed_records:
                record_type, *data = record
                if record_type.lower() == "news":
                    text, city = data  # Adjust unpacking for private ads
                    self.news_feed.add_news(text, city, current_date)
                elif record_type.lower() == "private_ad":
                    text, expiration_date = data
                    self.news_feed.add_private_ad(text, expiration_date, current_date)

            #os.remove(self.file_path)  # Remove the file after processing

    @staticmethod
    def normalize_case(text):
        return text.lower()

# Usage
file_path = r"C:\Users\dharm\PycharmProjects\epam_python_practice_repo\news_feed.txt"
news_processor = NewsFeedProcessor(file_path)
news_processor.process_records()




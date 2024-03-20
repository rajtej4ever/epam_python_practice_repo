import os
import csv
import datetime

class NewsFeed:
    def __init__(self):
        self.news_feed_file = "news_feed.txt"
        self.words = {}
        self.letters = {}

    def add_news(self, text, city, current_date):
        record = f"NEWS|{text}|{city}|{current_date}\n"
        self._append_to_file(record)
        self.update_word_and_letter_counts(text)

    def add_private_ad(self, text, expiration_date, current_date):
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        days_left = (expiration_date - current_date).days
        record = f"PRIVATE_AD|{text}|{expiration_date}|{days_left} days left\n"
        self._append_to_file(record)
        self.update_word_and_letter_counts(text)

    def _append_to_file(self, record):
        with open(self.news_feed_file, "a") as file:
            file.write(record)

    def update_word_and_letter_counts(self, text):
        # Update word count
        for word in text.split():
            word = word.lower()  # Convert to lowercase
            self.words[word] = self.words.get(word, 0) + 1

        # Update letter count
        for letter in text:
            if letter.isalpha():
                self.letters[letter.lower()] = self.letters.get(letter.lower(), 0) + 1

    def export_word_count_to_csv(self):
        word_count_file = "word_count.csv"
        with open(word_count_file, "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Word", "Count"])
            for word, count in self.words.items():
                csv_writer.writerow([word, count])

    def export_letter_count_to_csv(self):
        letter_count_file = "letter_count.csv"
        total_letters = sum(self.letters.values())
        with open(letter_count_file, "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Letter", "Count", "Count_uppercase", "Percentage"])
            for letter, count in self.letters.items():
                count_uppercase = sum(1 for char in letter if char.isupper())
                percentage = (count / total_letters) * 100 if total_letters != 0 else 0
                csv_writer.writerow([letter, count, count_uppercase, percentage])

    def clear_counts(self):
        self.words = {}
        self.letters = {}

class NewsFeedProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.news_feed = NewsFeed()

    def process_records(self):
        current_date = datetime.datetime.now()
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                records = file.readlines()

            for record in records:
                parts = record.strip().split("|")
                record_type = parts[0]
                data = parts[1:]

                if record_type.lower() == "news" and len(data) == 3:
                    text, city, _ = data
                    self.news_feed.add_news(text, city, current_date)
                elif record_type.lower() == "private_ad" and len(data) == 2:
                    text, expiration_date = data
                    self.news_feed.add_private_ad(text, expiration_date, current_date)
            #os.remove(self.file_path)  # Remove the file after processing

            # Export to CSV files
            self.news_feed.export_word_count_to_csv()
            self.news_feed.export_letter_count_to_csv()
            # Clear counts
            self.news_feed.clear_counts()

# Usage
file_path = r"C:\Users\dharm\PycharmProjects\epam_python_practice_repo\news_feed.txt"
news_processor = NewsFeedProcessor(file_path)
news_processor.process_records()

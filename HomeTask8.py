import os
import csv
import datetime
import json

class NewsFeed:
    def __init__(self):
        self.words = {}
        self.letters = {}

    def add_news(self, text, city, current_date):
        self.update_word_and_letter_counts(text)

    def add_private_ad(self, text, expiration_date, current_date):
        self.update_word_and_letter_counts(text)

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
        pass

    def export_letter_count_to_csv(self):
        pass

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
            os.remove(self.file_path)  # Remove the file after processing

            # Export to CSV files
            self.news_feed.export_word_count_to_csv()
            self.news_feed.export_letter_count_to_csv()
            # Clear counts
            self.news_feed.clear_counts()

class JSONNewsProvider:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def get_records(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, "r") as json_file:
                records = json.load(json_file)
            return records
        else:
            return []

# Usage
json_file_path = input("Enter JSON file path: ")
json_news_provider = JSONNewsProvider(json_file_path)
records = json_news_provider.get_records()

# Process records
for record in records:
    file_path = input("Enter file path: ")
    news_processor = NewsFeedProcessor(file_path)
    news_processor.process_records()

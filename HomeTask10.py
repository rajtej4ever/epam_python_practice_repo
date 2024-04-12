import os
import csv
import datetime
import json
import xml.etree.ElementTree as ET
import sqlite3

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

class XMLNewsProvider:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path

    def get_records(self):
        if os.path.exists(self.xml_file_path):
            tree = ET.parse(self.xml_file_path)
            root = tree.getroot()
            records = []
            for record in root.findall('record'):
                data = record.text.strip().split("|")
                records.append(data)
            return records
        else:
            return []

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.create_tables()

    def create_connection(self):
        self.connection = sqlite3.connect(self.db_file)
        self.connection.execute('PRAGMA foreign_keys = ON;')
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def create_tables(self):
        if not os.path.exists(self.db_file):
            self.create_connection()
            cursor = self.connection.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS news (
                                id INTEGER PRIMARY KEY,
                                text TEXT NOT NULL,
                                city TEXT NOT NULL,
                                date TEXT NOT NULL
                            );''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS private_ads (
                                id INTEGER PRIMARY KEY,
                                text TEXT NOT NULL,
                                expiration_date TEXT NOT NULL,
                                date TEXT NOT NULL
                            );''')

            self.connection.commit()
            self.close_connection()

    def insert_news_record(self, text, city, current_date):
        self.create_connection()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO news (text, city, date) VALUES (?, ?, ?);", (text, city, str(current_date)))
        self.connection.commit()
        self.close_connection()

    def insert_private_ad_record(self, text, expiration_date, current_date):
        self.create_connection()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO private_ads (text, expiration_date, date) VALUES (?, ?, ?);", (text, expiration_date, str(current_date)))
        self.connection.commit()
        self.close_connection()

# Usage
input_format = input("Enter input format (xml/json): ").lower()
if input_format == "xml":
    xml_file_path = input("Enter XML file path: ")
    xml_news_provider = XMLNewsProvider(xml_file_path)
    records = xml_news_provider.get_records()
elif input_format == "json":
    json_file_path = input("Enter JSON file path: ")
    json_news_provider = JSONNewsProvider(json_file_path)
    records = json_news_provider.get_records()
else:
    print("Invalid input format.")

# Process records and insert into database
db_file = "news_database.db"
db_manager = DatabaseManager(db_file)

for record in records:
    record_type = record[0].lower()
    if record_type == "news" and len(record) == 4:
        text, city, _, current_date = record
        db_manager.insert_news_record(text, city, current_date)
    elif record_type == "private_ad" and len(record) == 3:
        text, expiration_date, current_date = record
        db_manager.insert_private_ad_record(text, expiration_date, current_date)

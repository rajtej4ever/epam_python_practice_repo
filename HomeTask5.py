import datetime


class NewsFeed:
    def __init__(self):
        self.news_feed_file = "news_feed.txt"

    def add_news(self, text, city):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"NEWS|{text}|{city}|{current_date}\n"
        self._append_to_file(record)

    def add_private_ad(self, text, expiration_date):
        current_date = datetime.datetime.now()
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        days_left = (expiration_date - current_date).days
        record = f"PRIVATE_AD|{text}|{expiration_date}|{days_left} days left\n"
        self._append_to_file(record)

    def _append_to_file(self, record):
        with open(self.news_feed_file, "a") as file:
            file.write(record)

#usage
news_feed = NewsFeed()
news_feed.add_news("Modi is launching underwater metro station", "Kolkata")
news_feed.add_private_ad("Summer sale", "2024-03-15")
#news_feed.add_news("carnival in timesquare", "newyork")
#news_feed.add_private_ad("Covid 2024", "2024-03-15")

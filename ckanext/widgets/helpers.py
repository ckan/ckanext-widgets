from pylons import config
import feedparser


def fetch_feed(feed_url, number_of_entries=5):
    feed = feedparser.parse(feed_url)
    feed['entries'] = feed['entries'][:number_of_entries]
    return feed
    

def get_featured_feed():
    return config.get('ckanext.widgets.featured_feed')

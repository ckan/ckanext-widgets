from ckan.plugins import toolkit
from ckan.lib import search
from pylons import config
import feedparser
import socket


socket.setdefaulttimeout(10)


def fetch_feed(feed_url, number_of_entries=3):
    feed = feedparser.parse(feed_url)
    feed['entries'] = feed['entries'][:number_of_entries]
    return feed


def get_featured_feed():
    return config.get('ckanext.widgets.featured_feed')


def get_recently_updated_datasets(limit=3):
    try:
        return toolkit.get_action('package_search')(data_dict={
            'sort': 'metadata_modified desc',
            'rows': limit,
        })['results']
    except toolkit.ValidationError, search.SearchError:
        return []

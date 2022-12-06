import random

class ShortenerService(object):
    def __init__(self):
        self.urls_mapping = dict()

    def generate_short_url(self, raw_url):
        shortened_url = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
        # TODO - check for collision
        self.urls_mapping[shortened_url] = raw_url
        return shortened_url

    def get_raw_url(self, shortened_url):
        # TODO - validate if it's a valid shortened url
        return self.urls_mapping[shortened_url]


from scrapy.dupefilters import RFPDupeFilter
import hashlib
import json

def save_seen_requests(seen_requests, filename='seen_requests.json'):
    with open(filename, 'w') as f:
        json.dump(list(seen_requests), f)

def load_seen_requests(filename='seen_requests.json'):
    try:
        with open(filename) as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()


class MyDupeFilter(RFPDupeFilter):
    file_name = 'seen_requests.json'
    seen_requests = load_seen_requests(file_name)

    def request_seen(self, request):
        fp = self.request_fingerprint(request)
        if fp in self.seen_requests:
            return True
        self.seen_requests.add(fp)
        save_seen_requests(self.seen_requests, self.file_name)
        return False

    def request_fingerprint(self, request):
        return hashlib.sha1(request.url.encode()).hexdigest()

import json
import codecs

class WugCache:
    wc = {}
    _json_source: str = ""

    @staticmethod
    def init(json_source="wugplurals.json"):
        WugCache._json_source = json_source

        WugCache.updatecache()
    
    @staticmethod
    def updatecache():
        with codecs.open(WugCache._json_source, encoding="utf-8", mode='r') as f:
            WugCache.wc = json.loads(f.read())

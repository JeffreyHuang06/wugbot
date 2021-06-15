import json
from typing import Dict, List

class WugCache:
    wc: Dict[str, List[str]] = {}
    _json_source: str = ""

    @staticmethod
    def init(json_source="wugplurals.json"):
        WugCache._json_source = json_source

        WugCache.updatecache()
    
    @staticmethod
    def updatecache():
        with open(WugCache._json_source, 'r') as f:
            WugCache.wc = json.loads(f.read())

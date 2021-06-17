from src.wugcache import WugCache

def wccmd(func):
    def inner():
        WugCache.updatecache()
        func()
    
    return inner
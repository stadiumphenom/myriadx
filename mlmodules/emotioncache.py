# emotioncache.py
# Minimal cache to avoid reprocessing the same image repeatedly

import hashlib

_cache = {}

def _hash_path(image_path):
    return hashlib.md5(image_path.encode("utf-8")).hexdigest()

def check_cache(image_path):
    key = _hash_path(image_path)
    return _cache.get(key)

def store_in_cache(image_path, result):
    key = _hash_path(image_path)
    _cache[key] = result

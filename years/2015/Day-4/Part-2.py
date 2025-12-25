import hashlib
from itertools import count

for i in count():
    text = f"iwrupvqb{i}"
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    if md5_hash.startswith("000000"):
        print(i)
        break
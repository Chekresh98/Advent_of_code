import hashlib
from itertools import count

# text = "abcdef"
# md5_hash = hashlib.md5(text.encode()).hexdigest()
# print(md5_hash)

for i in count():
    text = f"iwrupvqb{i}"
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    if md5_hash.startswith("00000"):
        print(i)
        break

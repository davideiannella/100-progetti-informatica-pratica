import re
from collections import Counter
PATTERN = re.compile('^(?P<level>INFO|WARN|ERROR) (?P<method>GET|POST|PUT|DELETE) (?P<path>/\\S*) (?P<status>\\d{3})$')

def analyze(lines):
    levels = Counter()
    paths = Counter()
    status = Counter()
    malformed = 0
    for line in lines:
        m = PATTERN.match(line.strip())
        if not m:
            malformed += 1
            continue
        d = m.groupdict()
        levels[d['level']] += 1
        paths[d['path']] += 1
        status[int(d['status'])] += 1
    return {'levels': levels, 'paths': paths, 'status': status, 'malformed': malformed}

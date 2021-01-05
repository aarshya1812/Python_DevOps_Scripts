#!/usr/bin/env python3
"Read Log file and Search for CRON lines"
import sys
import re

if sys.argv[1]:
    logfile = sys.argv[1]
else:
    exit(1)

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        print('Found --->', line.strip())

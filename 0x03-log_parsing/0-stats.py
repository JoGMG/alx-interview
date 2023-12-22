#!/usr/bin/python3
"""
A script that reads `stdin` line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>` (if the format is not this one, the line
must be skipped)
- After every 10 lines and/or a keyboard interruption `(CTRL + C)`,
print these statistics from the beginning:
    • Total file size: `File size: <total size>`
    • where `<total size>` is the sum of all previous <file size>
    `(see input format above)`
    • Number of lines by status code:
        - possible status code: `200`, `301`, `400`, `401`, `403`,
        `404`, `405` and `500`
        - if a status code doesn't appear or is not an integer,
        don't print anything for this status code
        - format: `<status code>: <number>`
        - status codes should be printed in ascending order
"""
import sys


total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                status_counts[status_code] = \
                    status_counts.get(status_code, 0) + 1

            # Print stats after every 10 lines
            if i % 10 == 0:
                print(f"File size: {total_size}")
                for status_code in sorted(status_counts):
                    print(f"{status_code}: {status_counts[status_code]}")
except KeyboardInterrupt:
    pass  # Handle Ctrl+C

    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

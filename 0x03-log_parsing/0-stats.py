#!/usr/bin/python3

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display stats
    """
    print("Total file size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        count = log["code_frequency"][code]
        if count:
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = int(match.group(1))  # Convert code to integer
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # Status code
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        pass
    finally:
        output(log)

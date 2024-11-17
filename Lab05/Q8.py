import re

text = """This document was created on 12/09/2023. The last update was on 2023-09-12.
Our event will be on Sep 12, 2023, and another one on October 5, 2023.
Please confirm your availability by 2023-10-10 or 05/10/2023."""

date_pattern = r'((0?[1-9]|[12][0-9]|3[01])[-/](0?[1-9]|1[0-2])[-/](\d{4})|(\d{4})[-/](0?[1-9]|1[0-2])[-/](0?[1-9]|[12][0-9]|3[01])|([A-Za-z]{3,9})\s+(\d{1,2}),\s+(\d{4}))'

print(re.findall(date_pattern, text))
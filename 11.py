# pip install python-dateutil
from dateutil import parser

def parse_date(date_string):
    try:
        return parser.parse(date_string)
    except ValueError:
        raise ValueError(f"无法解析日期: {date_string}")

# 测试
dates = ['7/30/24', '07/30/24', '7/30/2024', '2024-07-30']
for date in dates:
    try:
        parsed_date = parse_date(date)
        print(f"原始日期: {date}, 解析后: {parsed_date}")
    except ValueError as e:
        print(e)
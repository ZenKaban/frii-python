import re

count_dict_date = {}
count_dict_url = {}
count_dict_response_code = {}

with open("parse.tsv", "r") as f:
    for line in f:
        date_re = re.search("\t([0-9]{9})", line)
        try:
            date = date_re.group(1)
        except:
            date = None
        
        try:
            count_date = count_dict_date[date]
            count_date += 1
            count_dict_date[date] = count_date
        except:
            count_dict_date[date] = 1

        url_re = re.search("(/[a-zA-Z/.-]+)\t[0-9]+", line)
        try:
            url = url_re.group(1)
        except:
            url = None
        
        try:
            count_url = count_dict_url[url]
            count_url += 1
            count_dict_url[url] = count_url
        except:
            count_dict_url[url] = 1
            
        response_code_re = re.search("/[a-zA-Z/.-]+\t([0-9]+)", line)
        try:
            response_code = response_code_re.group(1)
        except:
            response_code = None

        try:
            count_response_code = count_dict_response_code[response_code]
            count_response_code += 1
            count_dict_response_code[response_code] = count_response_code
        except:
            count_dict_response_code[response_code] = 1

date_count = 0
for date in count_dict_date:
    if date is None:
        continue
    else:
        count = count_dict_date[date]
        date_count = date_count + count

url_count = 0
for url in count_dict_url:
    if url is None:
        continue
    else:
        count = count_dict_url[url]
        url_count = url_count + count
    
response_code_count = 0
for response_code in count_dict_response_code:
    if response_code is None:
        continue
    else:
        count = count_dict_response_code[response_code]
        response_code_count = response_code_count + count
    
print(f"date - {date_count}, url - {url_count}, response code - {response_code_count}")
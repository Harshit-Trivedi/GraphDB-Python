import re

# open required csv and read it as a text string
with open('file2.csv', 'r') as f:
    my_csv_text = f.read()

# replace 'Less than' with LT
find_str = 'Less than'
replace_str = 'LT'

# substitute
new_csv_str_lt = re.sub(find_str, replace_str, my_csv_text)

# replace 'Single Tent' with ST
find_sstr = 'Single Tent'
replace_sstr = 'ST'

new_csv_str_st = re.sub(find_sstr, replace_sstr, new_csv_str_lt)

# open new file and save changes
new_csv_path = 'file3.csv' # or whatever path and name you want
with open(new_csv_path, 'w') as f:
    f.write(new_csv_str_st)

print("Writing Complete")

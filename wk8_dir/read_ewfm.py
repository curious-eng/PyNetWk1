
import re

with open('ewfm2.txt','r') as fh:
     all_lines = fh.readlines()

my_master_list = []
jb_count = 0
for a in all_lines:
    my_ip_list = re.findall('\d+\.\d+\.\d+\.\d+\.\d+', a)
    for b in my_ip_list:
        my_master_list.append(re.findall('\d+\.\d+\.\d+\.\d+', b)[0])
    #print(a, my_ip_list)
#    jb_count += 1
#    if jb_count == 10:
#        print(my_master_list)
#        b = 1 / 0
dedup_list = list(set(my_master_list)) 
print(dedup_list)

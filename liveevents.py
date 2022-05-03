# 2022-02-10,07:16:54,208,event_6
# 2022-02-10,07:16:56,206,event_7

infile = r"C:\Users\byark\Documents\Codes\Python\liveevents.log"

user_id_list = []
unique_user_ids = []
dict = {}

with open(infile) as f:
    f = f.readlines()

for i in f:
    user_id_list.append(i.split(',')[2])

# print(user_id_list)

# for j in user_id_list:
#     if j not in unique_user_ids:
#         unique_user_ids.append(j)

# print(unique_user_ids)

mysum = 0

for j in user_id_list:
    if not j in dict:
        dict[j] = 1
    else: 
        dict[j] += 1

    mysum += 1

print(dict)
print(mysum)

# some events are in the future, filter out the events from the future mark as error 11.02.2022 14:06
param = {
    "(" : ")", 
    "{" : "}", 
    "[" : "]"
}

s = input("s = ")
s = s.replace('"', '')  # Removes all occurrences of double quotes
sNew = s 
valid = False

s_len = len(s)
print(s_len)
count = 0

check = True

# while count < (s_len - 1):
#     if s[count] in param:
#         if s[count + 1] == param[s[count]]: 
#             print(s[count],param[s[count]])
#             valid = True
#         else:
#             valid = False
#     else:
#         valid = False
#     count += 1

# print(valid)

while count < (s_len):
    # print(count, s[count])
    if sNew[count] in param:
        valid = False
        index1 = sNew.index(sNew[count])
        if param[sNew[count]] in sNew[index1: ]:
            valid = True
            # print(count, s[index1: ])
            index2 = sNew.index(param[sNew[count]])
            diff = (index2 - index1)
            sNew = sNew.replace(sNew[count], '')
            sNew = sNew.replace(param[sNew[count]], '')
            print(valid, sNew)

            if diff % 2 == 0:
                print("yo")
                valid = False
                break
        else: 
            valid = False
            print(valid)
    # else: 
    #     valid = False
    count += 1

print(valid)
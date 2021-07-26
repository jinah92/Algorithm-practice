data_list = list(map(int, input().split(' ')))
if sorted(data_list) == data_list:
    print("ascending")
elif sorted(data_list, reverse=True) == data_list:
    print("descending")
else:
    print("mixed")

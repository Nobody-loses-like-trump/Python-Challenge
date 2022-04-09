import pickle

with open("banner.pkl", "rb") as f:
    data = pickle.load(f)
    # print(data)

# def space_hash(list_100: list):
#     a = list_100[0] == " "
#     if a:
#         for index, value in enumerate(list_100):
#             if value != (index % 2)*"#" + ((index + 1) % 2)*" ":
#                 return '''False: " "'''
#     else:
#         for index, value in enumerate(list_100):
#             if value != (index % 2)*" " + ((index + 1) % 2)*"#":
#                 return '''False: "#"'''
#     return '''True: " "''' if a else '''True: "#"'''


# for i in data:
#     list_1 = list(zip(*i))[1]
#     list_0 = list(zip(*i))[0]
#     print(list_0)
#     # print(space_hash(list_0))
#     print()
#     print(list_1)
#     # print(sum(list_1))
#     # print(True if sum(list_1) == 95 else False)
#     print("-------------------------------------------------------------------")

# print(data)
for i in data:
    for j in i:
        print(j[0]*j[1], end="")
    print()

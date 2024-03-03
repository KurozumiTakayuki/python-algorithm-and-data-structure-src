my_dict = dict()

# キーを指定してデータを格納する
my_dict["tanaka"] = "tanaka@example.com"
print(my_dict)

# キーを指定してデータを取り出す
mail = my_dict["tanaka"]
print(mail)

# キーを指定してデータを削除する
del my_dict["tanaka"]
print(my_dict)

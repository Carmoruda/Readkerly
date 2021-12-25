import shelve

shelfFile = shelve.open("user_data")
print(shelfFile["user"])
shelfFile.close()

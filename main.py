#
try:
    filobj =  open("users.txt", 'r')

    for line in filobj:
        print(line)
    filobj.close()
except Exception as e:
    print(e)
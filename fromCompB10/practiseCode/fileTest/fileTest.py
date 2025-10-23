# strText = "This is some text.\n"
#
# myFile = open("textfile.txt", "r")
# # myFile.write(strText)
# # myFile.close()
# try:
#     strText  = myFile.read()
#     print(strText)
# except:
#     print("There is some error")
# finally:
#     myFile.close()

import os
os.remove('textfile.txt')
if os.path.exists('textfile.txt'):
    print('text file exists')
else:
    print('text file does not exist')
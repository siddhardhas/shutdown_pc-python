import os
shutdown=input("Do you what to shutdown your pc(yes/no):")
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    print("you declined to shutdown")
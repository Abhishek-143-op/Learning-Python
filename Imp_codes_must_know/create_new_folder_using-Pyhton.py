import os 
#Specifing the path of the folder 
Folder_path = "Imp_codes_must_know"

#checking weather if the folder already exists or not 
if not os.path.exists(Folder_path):
    os.makedirs(Folder_path)
    print("Folder created at ",Folder_path)
else:
    print("Folder at path already exists ")
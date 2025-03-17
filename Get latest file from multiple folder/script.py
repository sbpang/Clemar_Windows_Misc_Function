import os,re,shutil

output_Path = r'D:\20230626'

def filter_Backup_Models(file_Path):
    for root, dirs, files in os.walk(file_Path):
        for file in files:
            if file.endswith(".rvt"):
                if re.search(r"\.[0][0-9]{3}\.",file) == None: #20230207 updated

                    full_Path.append(os.path.join(root, file))
                    relative_Path.append(os.path.join(root, file).replace(file_Path,""))

                    try:
                        if file not in file_Name_Path.keys():
                        
                            file_Name_Path[file]=os.path.join(root, file)
                        else:
                            file_Name_Path[file]=file_Name_Path[file]+'\n'+os.path.join(root, file)
                    except KeyError:
                        pass

    return full_Path,relative_Path,file_Name_Path

def validate_File_Name(file_Name):
    if re.search(r"[a-z][A-Z][0-9]\_[a-z][A-Z]\_[a-z][A-Z]\_",file_Name) != None:
        return True
    else:
        return False

def get_folders_in_directory(directory):
    folder_Path,folder_Names = [],[]
    for entry in os.scandir(directory):
        if entry.is_dir():
            folder_Names.append(entry.path.split('\\')[-1])
            folder_Path.append(entry.path)
    return folder_Path,folder_Names

full_Path,relative_Path,file_Name_Path = [],[],{}

prefix = r"\\vircon_Station\P0276_SD3222-002_ASD"
suffix = r"30_As-Built_BIM\04_Floor_level"

sites = ['01 Tsuen Wan Government Primary School','02 Tsing Yi Municipal Services Building',
         '03 Education Services Centre at Kowloon Tong Public Transport Interchange','04 Trade and Industry Tower','05 Tsing Chau Street Customs Staff Quarters',
         '07 Che Kung Temple Sports Centre','08 Yuen Chau kok Complex','09 Former Chung Ancestral Hall','12 Old House of the Former Hoi Pa Tsuen']

for site in sites:
    # Specify the root directory where .rvt files are located
    root_Path = os.path.join(prefix,site,suffix)
    full_Path,relative_Path,file_Name_Path = filter_Backup_Models(root_Path)

for k,v in file_Name_Path.items():
    #print(k+':')
    i = [os.path.getmtime(v) for v in v.split('\n')].index((max([os.path.getmtime(v) for v in v.split('\n')])))
    latest_Path = v.split('\n')[i]
    #print('\n')
    output_Folder_Paths,output_Folder_Names = get_folders_in_directory(output_Path)

    for output_Folder_Path,output_Folder_Name in zip(output_Folder_Paths,output_Folder_Names):
        if output_Folder_Name in latest_Path:
            #print(k+':')
            #print(latest_Path)
            #print(output_Folder_Name)
            #print('\n')
            source_file = latest_Path
            destination_file = os.path.join(output_Folder_Path,k)
            print('Copying file from:')
            print(source_file)
            print('to:')
            print(destination_file)
            print('\n')
            shutil.copy(source_file, destination_file)
               
    




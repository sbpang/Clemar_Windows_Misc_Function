#####################################################################
#step 1. Parameter
root_Path = r"\\xxxx\yyyy\Clement\CIC BIM Object"
web_Crawler_Folder = "test1" #"Web Crawler"
other_Folder_Name = "OTHER"
ava_Format = ['rfa','rvt','pdf','dwg','pkt','txt']
#####################################################################
import os,shutil,itertools,re,time
from operator import itemgetter

def create_Folder(root_Path,local_Path):
    if isinstance(local_Path,list):
        if not os.path.exists(root_Path + os.sep + os.sep.join(local_Path)):
            try:
                os.makedirs(root_Path + os.sep + os.sep.join(local_Path))
            except OSError:#FileExistsError
                pass
        else:
            pass
    else:
        if not os.path.exists(root_Path + os.sep + local_Path):
            try:
                os.mkdir(root_Path + os.sep + local_Path)
            except OSError:
                pass
        else:
            pass

def copy(src,dst):
    shutil.copy2(src, dst)

def get_Naming_Sector(root_Path,web_Crawler_Folder):
    rfa_Path= {}
    orig_Lt,format_Lt,eq_Code_Lt,func_Type_Lt,des_Lt = [],[],[],[],[]

    for root, dirs, files in os.walk(root_Path + os.sep + web_Crawler_Folder):
        for file in files:
            
            if file.split(".")[-1].lower() in ava_Format:
            #########################################
            #1.1 get originator from -3-    
                if re.match(r"[a-z]{3,10}", file.split("-")[2].lower()):
                    originator = file.split("-")[2]
                else:
                    originator = other_Folder_Name

            #########################################
            #1.2 get file format .xxx
                file_Format = file.split(".")[-1]
                format_Lt.append(file_Format)

            #########################################
            #1.3 get Equipment Code -1-
                if not "BIM Object Sheet (" in file.split("-")[0]:
                    eq_Code = file.split("-")[0]
                    eq_Code_Lt.append(eq_Code)
                else:
                    eq_Code = file.split("-")[0].split("(")[-1]
                    eq_Code_Lt.append(eq_Code)
            
            #########################################
            #1.4 get function type -2-
                func_Type = file.split("-")[1]
                func_Type_Lt.append(func_Type)

            #########################################
            #1.5 Descriptor
                descriptor = "-".join(file.split("-")[(-len(file.split("-"))+3):]).split(")")[0].split(".")[0]
                des_Lt.append(descriptor)

            #########################################
            #2 combine data list creation
                if "." not in originator: 
                    orig_Lt.append(originator)
                    rfa_Path[file] = [originator,eq_Code,func_Type,descriptor,file_Format]
                else:
                    orig_Lt.append(originator)
                    rfa_Path[file] = [other_Folder_Name,eq_Code,func_Type,descriptor,file_Format]
    
    return rfa_Path

#################################################
#3 create required folder
def create_Folder_and_Nested(root_Path,folder_Lt):
    for indv in folder_Lt:
        sublist = [indv[0]]
        create_Folder(root_Path,sublist)
        for i in range(len(indv)-1):
            i = i + 1
            sublist.append(indv[i])
            create_Folder(root_Path,sublist)

#################################################
#4 copy to corresponding folder
def copy_wrt_Dict(root_Path,web_Crawler_Folder,rfa_Path):
    url = []
    if isinstance(rfa_Path,dict):
        for file_Name,file_Path in rfa_Path.items():
            try:
                src_path = root_Path + os.sep + web_Crawler_Folder + os.sep + file_Name
                dst_path = root_Path + ''.join([os.sep + file_Path[i] for i in range(len(file_Path))]) + os.sep + file_Name
                copy(src_path,dst_path)
                url.append(root_Path + ''.join([os.sep + file_Path[i] for i in range(len(file_Path))]))
            except:
                pass
    return url

#################################################


if __name__ == "__main__":
    
    ######################################
    #Step 2. Create folder
    start = time.time()

    rfa_Path = get_Naming_Sector(root_Path,web_Crawler_Folder)
    create_Folder_and_Nested(root_Path,rfa_Path.values())
    url_Lt = copy_wrt_Dict(root_Path,web_Crawler_Folder,rfa_Path)




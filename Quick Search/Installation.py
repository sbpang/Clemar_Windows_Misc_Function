import winreg as reg,shutil,sys,os
import ctypes

install_path = r'C:\ProgramData\Clemar Cloud\QuickSearch'
registry_name = 'QuickSearch'
exe_Name = 'QuickSearch.exe'
ico_Name = 'QuickSearch.ico'


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

def add_to_context_menu(registry_name,install_path,exe_Name,ico_Name):
    # Path to the context menu name
    key_path = r'Directory\\Background\\shell\\' + registry_name
    
    # Key to execute Quicksearch.exe
    key_path_cmd = key_path + r'\\command'
    
    # Path to Quicksearch.exe in C:\ProgramData
    exe_path = os.path.join(install_path, exe_Name)
    icon_path = os.path.join(install_path, ico_Name)
    
    # Try to create/open the key
    try:
        reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        registry_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path, 0, reg.KEY_WRITE)
        
        # Name that will appear in the context menu
        #reg.SetValue(registry_key, '', reg.REG_SZ, 'Quick Search')
        if icon_path:
            reg.SetValueEx(registry_key, 'Icon', 0, reg.REG_SZ, icon_path)
        reg.CloseKey(registry_key)
        
        # Set the command for the context menu item
        reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path_cmd)
        registry_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path_cmd, 0, reg.KEY_WRITE)
        
        # Command that will run when the context menu item is clicked
        reg.SetValue(registry_key, '', reg.REG_SZ, exe_path + ' "%V"')
        reg.CloseKey(registry_key)
        
    except WindowsError:
        print("Failed to add to context menu. Try running as administrator.")
        sys.exit(1)


def copy_quicksearch(exe_name,ico_name):
    # Path to Quicksearch.exe within the bundle
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(bundle_dir, exe_name)
    icon_path = os.path.join(bundle_dir, ico_name)
    
    # Path to where Quicksearch.exe should be copied    
    dest_exe_path = os.path.join(install_path, exe_name)
    dest_icon_path = os.path.join(install_path, ico_name)
    
    # Ensure the target directory exists
    if not os.path.exists(install_path):
        os.makedirs(install_path)

    try:
        shutil.copy(src_path, dest_exe_path)
        shutil.copy(icon_path, dest_icon_path)

    except PermissionError:
        print("Failed to copy Quicksearch.exe. Try running as administrator.")
        sys.exit(1)


if ctypes.windll.shell32.IsUserAnAdmin():
    copy_quicksearch(exe_Name,ico_Name)
    add_to_context_menu(registry_name,install_path,exe_Name,ico_Name)
    print("Installation completed successfully!")
    input("Press Enter to continue...")
else:
    # Re-run the script with admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)




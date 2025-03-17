import winreg as reg, sys, os
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

def remove_from_context_menu(registry_name):
    # Path to the context menu name
    key_path = r'Directory\\Background\\shell\\' + registry_name
    
    # Try to delete the key
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path + r'\\command')
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
    except WindowsError:
        print("Failed to remove from context menu. Try running as administrator.")
        sys.exit(1)

def delete_quicksearch_files(exe_name, ico_name):
    exe_path = os.path.join(install_path, exe_name)
    ico_path = os.path.join(install_path, ico_name)
    
    try:
        if os.path.exists(exe_path):
            os.remove(exe_path)
        if os.path.exists(ico_path):
            os.remove(ico_path)
    except PermissionError:
        #print("Failed to delete files. Try running as administrator.")
        sys.exit(1)

if ctypes.windll.shell32.IsUserAnAdmin():
    remove_from_context_menu(registry_name)
    delete_quicksearch_files(exe_Name, ico_Name)
    print("Uninstallation completed successfully!")
    input("Press Enter to continue...")
else:
    # Re-run the script with admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
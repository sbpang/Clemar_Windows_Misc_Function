import winreg as reg,shutil,sys,os

"""def add_to_context_menu_py(script_path, menu_name="SearchFiles", icon_path=None):
    # Define the path to the registry key
    reg_key = r'Directory\Background\shell'
    key_path = f"{reg_key}\\{menu_name}"

    # Connect to the registry
    reg_key = reg.ConnectRegistry(None, reg.HKEY_CLASSES_ROOT)

    # Create a new key for the context menu item
    reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)

    # If an icon is provided, set the icon for the context menu item
    if icon_path:
        reg.SetValueEx(reg_key, "Icon", 0, reg.REG_SZ, icon_path)

    # Create a new key for the command of the context menu item
    command_key = reg.CreateKey(reg_key, "command")

    # Set the command for the context menu item
    python_path = r"C:\ProgramData\anaconda3\pythonw.exe"  # Replace with your Python path
    reg.SetValueEx(command_key, "", 0, reg.REG_SZ, f'"{python_path}" "{script_path}" "%V"')

    # Close the registry keys
    reg.CloseKey(command_key)
    reg.CloseKey(reg_key)
"""

"""def add_to_context_menu(script_path, menu_name="SearchFiles", icon_path=None):
    # Define the path to the registry key
    reg_key = r'Directory\Background\shell'
    key_path = f"{reg_key}\\{menu_name}"

    # Connect to the registry
    reg_key = reg.ConnectRegistry(None, reg.HKEY_CLASSES_ROOT)

    # Create a new key for the context menu item
    reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)

    # If an icon is provided, set the icon for the context menu item
    if icon_path:
        reg.SetValueEx(reg_key, "Icon", 0, reg.REG_SZ, icon_path)

    # Create a new key for the command of the context menu item
    command_key = reg.CreateKey(reg_key, "command")

    # Set the command for the context menu item
    reg.SetValueEx(command_key, "", 0, reg.REG_SZ, f'"{script_path}" "%V"')

    # Close the registry keys
    reg.CloseKey(command_key)
    reg.CloseKey(reg_key)"""

def add_to_context_menu():
    # Path to the context menu name
    key_path = r'Directory\\Background\\shell\\Quicksearch'
    
    # Key to execute Quicksearch.exe
    key_path_cmd = key_path + r'\\command'
    
    # Path to Quicksearch.exe in C:\ProgramData
    quicksearch_exe_path = r'C:\ProgramData\Clemar Studio\Quicksearch.exe'
    
    # Try to create/open the key
    try:
        reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        registry_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path, 0, reg.KEY_WRITE)
        
        # Name that will appear in the context menu
        reg.SetValue(registry_key, '', reg.REG_SZ, 'Quick Search')
        reg.CloseKey(registry_key)
        
        # Set the command for the context menu item
        reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path_cmd)
        registry_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path_cmd, 0, reg.KEY_WRITE)
        
        # Command that will run when the context menu item is clicked
        reg.SetValue(registry_key, '', reg.REG_SZ, quicksearch_exe_path + ' "%V"')
        reg.CloseKey(registry_key)
        
    except WindowsError:
        print("Failed to add to context menu. Try running as administrator.")
        sys.exit(1)

def copy_quicksearch():
    # Path to Quicksearch.exe within the bundle
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(bundle_dir, 'Quicksearch.exe')
    
    # Path to where Quicksearch.exe should be copied
    dest_path = r'C:\ProgramData\Clemar Studio\Quicksearch.exe'
    
    try:
        shutil.copy(src_path, dest_path)
    except PermissionError:
        print("Failed to copy Quicksearch.exe. Try running as administrator.")
        sys.exit(1)

if __name__ == "__main__":
    copy_quicksearch()
    add_to_context_menu()
    print("Installation completed successfully!")

#if __name__ == "__main__":
    #script_path = r"D:\Python\Window Misc Function\Quick Search\QuickSearch.py"
    #script_path = r"D:\Python\Window Misc Function\Quick Search\QuickSearch.exe"
    #icon_path = r"D:\Python\Window Misc Function\Quick Search\icon.ico"  # Optional
    #add_to_context_menu(script_path, menu_name="SearchFiles", icon_path=icon_path)

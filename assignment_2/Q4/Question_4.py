import os

def list_files_in_folder(folder_path, indent=0):
   
    try:
        items = os.listdir(folder_path)
    except PermissionError:
        print(f"{' ' * indent}Permission denied: {folder_path}")
        return
    except FileNotFoundError:
        print(f"{' ' * indent}Folder not found: {folder_path}")
        return

   
    for item in items:
        full_path = os.path.join(folder_path, item)
        
       
        if os.path.isfile(full_path):
            print(f"{' ' * indent}{item}")
        
        
        elif os.path.isdir(full_path):
            print(f"{' ' * indent}>>{item}/")  
            list_files_in_folder(full_path, indent + 4)  


folder = input("Enter the folder path: ")


list_files_in_folder(folder)

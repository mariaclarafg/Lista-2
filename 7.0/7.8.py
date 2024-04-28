import shutil

def delete_temp_directory():
    try:
        shutil.rmtree("temp")
        print("Directory 'temp' and its contents have been deleted successfully.")
    except FileNotFoundError:
        print("Directory 'temp' not found.")

delete_temp_directory()
import os
import shutil
from datetime import datetime

print("=" * 50)
print("      FILE AUTOMATION SYSTEM")
print("=" * 50)

source_folder = r"C:\Users\Glats\Pictures\source"
destination_folder = r"C:\Users\Glats\Pictures\destination"

files = os.listdir(source_folder)

moved_count = 0

for file in files:
    if file.endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        moved_count += 1

        current_time = datetime.now().strftime("%H:%M:%S")

        print(f"[{current_time}] {file} moved successfully")

print("\n" + "=" * 50)
print(f" TOTAL FILES MOVED : {moved_count}")
print(" AUTOMATION COMPLETED SUCCESSFULLY")
print("=" * 50)
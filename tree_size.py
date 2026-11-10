import os
folder_path = input("Enter folder path: ")
def tree_size(folder_path):
    total_size = 0
    file_count = 0
    directories = []

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            file_count += 1
            total_size += os.path.getsize(item_path)
        elif os.path.isdir(item_path):

            sub_size, sub_count, sub_directories = tree_size(item_path)
            total_size += sub_size
            file_count += sub_count
            directories.append((item_path, sub_size, sub_count))
    directories = sorted (directories,  key=lambda x: x[1],reverse=True)

    return total_size, file_count, directories

total_size, file_count, directories = tree_size(folder_path)

size_gb = total_size / (1024 ** 3)
print("total_size:", f"{size_gb:>10.2f}", "GB")
print("file_count:", file_count)

def print_tree(folder_path, level=0):
    total_size, file_count, directories = tree_size(folder_path)

    for item_path, sub_size, sub_count in directories:

            size_gb = sub_size / (1024 ** 3)

            indent = "|  " * level

            print(f"{item_path:<30}",indent + "---+", f"{size_gb:>10.2f}", "GB", f"{sub_count:>20}", "files")

            print_tree(item_path, level + 1)

print_tree(folder_path)









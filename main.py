
import parafin_files


directory = "."

print("Усі файли:")
print(parafin_files.list_files(directory))

print("Файли, у назві яких є parafin:")
print(parafin_files.find_files(directory, "parafin"))

file_path = "ivan_parafin_it-32.txt"
text = "Ivan Parafin, IT-32"

parafin_files.create_file(file_path, text)
print("Створено файл:", file_path)

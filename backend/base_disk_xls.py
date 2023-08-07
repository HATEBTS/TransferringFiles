from os import walk, path, listdir

paths = r"C:\Users\1\Desktop\last"
dict_base_path = {
    "Звено": [],
    "Номер акта": [],
    "Статус акта": [],
    "Статус видео": [],
    "Кол-во видео": [],
    "Статус РД": [],
    "Ссылка на папку": []
}


import os


def unload_disk_base(dirs):
    for root, dirs, files in os.walk(os.path.abspath(dirs)):
        for file in files:
            path_file = os.path.join(root, file).split('\\')
            zv = path_file[-3][:2]
            num_act = path_file[-3][:5]
            # print(num_act)
            if "Акты" in path_file:
                pass
                print(path_file, zv, num_act)
            else:
                print(path_file, 'no')

            # if "Видео" in path_file:
            #     print(path_file, zv, num_act)



print(unload_disk_base(paths))

# >>> df = pd.DataFrame({
# ...     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
# ...     'population': [17.04, 143.5, 9.5, 45.5],
# ...     'square': [2724902, 17125191, 207600, 603628]
# ... })
# >>> df
#    country  population    square
# 0  Kazakhstan       17.04   2724902
# 1      Russia      143.50  17125191
# 2     Belarus        9.50    207600
# 3     Ukraine       45.50    603628

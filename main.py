import json
def cards_import(file_path_full_name):
    with open(file_path_full_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    # беру только значения словаря, значения преобразовываю из строки в словарь
    data_dict = eval(data.get('data'))
    # вытягиваю отдельно карточки дтп
    cards_str = data_dict.get("cards")

    print(type(cards_str))
    return cards_str

br_2024 = r"C:\Users\vikto\Downloads\gbbd_stats_analysis\dtpdata\2024\15 Брянская область 1-7.2024.json"
br_2023 = r"C:\Users\vikto\Downloads\gbbd_stats_analysis\dtpdata\2023\15 Брянская область 1-12.2023.json"

spb_2024 = r"C:\Users\vikto\Downloads\gbbd_stats_analysis\dtpdata\2024\40 г. Санкт-Петербург 1-7.2024.json"
spb_2023 = r"C:\Users\vikto\Downloads\gbbd_stats_analysis\dtpdata\2023\40 г. Санкт-Петербург 1-12.2023.json"

msk_2024 = r"C:\Users\vikto\Downloads\gbbd_stats_analysis\dtpdata\2024\45 г. Москва 1-7.2024.json"
msk_2023 = r"C:\Users\vikto\Downloads\gbbd_stats_analysis\dtpdata\2023\45 г. Москва 1-12.2023.json"

br_2024_py = cards_import(br_2024)
br_2023_py = cards_import(br_2023)

spb_2024_py = cards_import(spb_2024)
spb_2023_py = cards_import(spb_2023)

msk_2024_py = cards_import(msk_2024)
msk_2023_py = cards_import(msk_2023)


print(type(br_2023_py[1]))

# Список, состоит из словарей. Мне нужно, чтобы программа бежала по всему списку словарей
# и из каждого словаря брала данные.
# Эти данные должны быть записаны в строки таблицы пандас. В таблице уже должны быть нужные столбцы.


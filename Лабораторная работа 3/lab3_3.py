# TODO  Напишите функцию count_letters
def count_letters(str):
    main_split = str.split()
    letter_join = ''.join(main_split)
    for i in letter_join:
        if i.isalpha() is False:
            letter_join = letter_join.replace(i, '')
    letter_join_low = letter_join.lower()
    letter_list = list(letter_join_low)
    letter_list.sort()
    print(letter_list)
    list_l = list(letter_join_low)
    set_letter = set(list_l)
    list_letter = list(set_letter)
    list_numbers = []
    for letter in set_letter:
        letter_join_low.count(letter)
        letters_numbers = letter_join_low.count(letter)
        letters_numbers = float(letters_numbers)
        list_numbers.append(letters_numbers)

    #print(list_numbers)
    #print(list_letter)
    dict_letter = dict(zip(list_letter, list_numbers))
    numbers = len(letter_join_low)
    #print(dict_letter)
    #print(numbers)
    return dict_letter



# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict):
    key = []
    numbers = []
    for key_d in dict.keys():
        key.append(key_d)
    for number_d in dict.values():
        numbers.append(number_d)
    print(key)
    print(numbers)


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
count_letters(main_str)
# TODO Распечатайте в столбик букву и её частоту в тексте
#calculate_frequency(count_letters(main_str))

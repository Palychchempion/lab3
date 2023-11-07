# TODO  Напишите функцию count_letters

def count_letters(str_1):
    str_1 = str_1.lower()
    list_divided = str_1.split()
    dict_1 = {}
    for i in range(len(list_divided)):
        str_help = list_divided[i]
        for j in range(len(str_help)):
            if str_help[j].isalpha():
                if str_help[j] in dict_1:
                    dict_1[str_help[j]] += 1
                else:
                    dict_1[str_help[j]] = 1
            else:
                continue
    return dict_1


# TODO Напишите функцию calculate_frequency

def calculate_frequency(letters):
    count_letter = sum(letters.values())
    for letter, key in letters.items():
        letters[letter] = round(key / count_letter, 2)
    return letters


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

dict_end = calculate_frequency(count_letters(main_str))
for letter, key in dict_end.items():
    if key == 0.0:
        print(letter+':',"0.00")
    else:
        print(letter+':',key)

# TODO Распечатайте в столбик букву и её частоту в тексте

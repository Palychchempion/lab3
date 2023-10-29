# Выполнение третьего задания
def count_letters(text):
    text = text.lower()
    dictionary = {chr(j): 0 for j in range(1072, 1104)}
    for i in range(len(text)):
        try:
            dictionary[text[i]] += 1
        except:
            pass
    return dictionary

def calculate_frequency(dictionars):
    letters = 0
    for i in dictionars:
        letters += dictionars[i]
    for i in dictionars:
        dictionars[i] /= letters
    return dictionars


Text = "Вы работаете над проектом по анализу текстов, и вам нужно провести частотный анализ букв в заданном тексте." \
       "Частотный анализ поможет вам определить, какие буквы встречаются чаще всего, и построить статистику их использования."

dicts = calculate_frequency(count_letters(Text))
for i in dicts:
    print(f"{i}: {round(dicts[i], 2)}")


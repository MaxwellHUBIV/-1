def count_letters(main_text):
    symbol_dict = {}

    for symbol in main_text:
        if symbol.isalpha():
            symbol = symbol.lower()
            if symbol in symbol_dict:
                symbol_dict[symbol] += 1
            else:
                symbol_dict[symbol] = 1
    
    return symbol_dict

def calculate_frequency(symbols_dict_template):
    symbols_dict = {}

    sum_of_letters = sum(symbols_dict_template.values())
    for letter_index, count in symbols_dict_template.items():
        symbols_dict[letter_index] = count/sum_of_letters

    return symbols_dict

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

symbols_ = count_letters(main_str)
symbols_freq = calculate_frequency(symbols_)

for index, value in symbols_freq.items():
    print(f'{index}: {value:.2f}')


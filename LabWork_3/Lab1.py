# TODO Напишите функцию для поиска индекса товара
def find_index(item_list, needed_item):
    #print(needed_item)
    for item in item_list:
        if item == needed_item:
            return item_list.index(item)



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    #print(find_item)
    index_item = find_index(items_list, find_item)

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

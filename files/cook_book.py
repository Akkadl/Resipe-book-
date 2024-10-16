import os

def read_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            num_ingredients = int(file.readline().strip())
            ingredients = []
            for _ in range(num_ingredients):
                ingredient_data = file.readline().strip().split(' | ')
                ingredient_name, quantity, measure = ingredient_data
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': quantity
                    }
    return shop_list

def merge_files(file_names, output_file):
    file_data = []
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((file_name, len(lines), lines))
    
    file_data.sort(key=lambda x: x[1])
    
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_name, line_count, lines in file_data:
            result_file.write(f"{file_name}\n{line_count}\n")
            result_file.writelines(lines)

if __name__ == '__main__':
    cook_book = read_recipes('files/recipes.txt')
    print("Кулинарная книга:", cook_book)
    
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
    print("\nСписок покупок:", shop_list)
    

    file_names = ['files/1.txt', 'files/2.txt']
    merge_files(file_names, 'files/result.txt')
    print("\nФайлы объединены и сохранены в 'result.txt'")

from django.shortcuts import render
# from django.shortcuts import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def dish(request):
    quantity = {}
    name_dish = request.get_full_path().split('/')[1]
    servings = request.GET.get('servings')
    if not servings:
        servings = 1
    else:
        servings = int(servings)
    for ingredients in DATA[name_dish]:
        quantity[ingredients] = DATA[name_dish][ingredients] * servings
    context = {
        'recipe': {name_dish: quantity}
    }
    print(type(request))
    return render(request, 'calculator/index.html', context)
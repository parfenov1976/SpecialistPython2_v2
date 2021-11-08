# "Друзья друзей"
# У всех людей, по крайне мере я надеюсь, есть друзья. У ваших друзей тоже есть друзья и так далее.
# Вы решили запустить свой бизнес и пригласить максимальное количество людей на его открытие.
# Вам в руки попала, как нельзя кстати, база людей со списком их друзей.
# Считаем, что комбинация Имя+Фамилия нам позволяет однозначно идентифицировать человека.

# Задача
# По предоставленным данным(файл peoples.json) определите:
# 1. Сколько людей придет на открытие, если вы отправляете приглашение конкретному человеку
# (любому, на ваш выбор, из базы), а тот всем друзьям, друзья друзьям и т.д.

# 2. Какому минимальному числу людей, нужно отправить приглашение,
# чтобы пришли ВСЕ люди, присутствующие в базе?


# Сюда отправляем полное решение
import os
import json


def dfs(v):
    visited[visited.index(
        list(filter(lambda x: x['name'] == v['name'] and x['surname'] == v['surname'], visited))[0])
    ]['visited'] = True
    # print(json.dumps(visited, sort_keys=False, indent=4, ensure_ascii=False))
    for w in read_data[read_data.index(
            list(filter(lambda x: x['name'] == v['name'] and x['surname'] == v['surname'], read_data))[0])
    ]['friends']:
        # print('======', w)
        if list(filter(lambda x: x['name'] == w['name'] and x['surname'] == w['surname'], visited)):
            if not visited[visited.index(
                    list(filter(lambda x: x['name'] == w['name'] and x['surname'] == w['surname'], visited))[0])
            ]['visited']:  # посещён ли текущий сосед?
                dfs(w)


with open(os.path.join('peoples.json'), 'r', encoding='UTF-8') as f:
    read_data = json.load(f)


# 1-ое задание
visited = []
for el in read_data:
    visited.append({'name': el['name'], 'surname': el['surname'], 'visited': False})

print('Кому отправить приглашение?:')
for el in visited:
    print(f'{visited.index(el) + 1} - {el["name"]} {el["surname"]}')
selection = int(input('Укажите номер: '))
visited.insert(0, visited.pop(selection - 1))
start = visited[0]
dfs(start)
print('Начало вывода результатов по 1-му заданию')
print(json.dumps(visited, sort_keys=False, indent=4, ensure_ascii=False))
print('Конец вывода результатов по 1-му заданию')

# 2-ое задание
list_to_invite = []
to_visit = []
for el in read_data:
    to_visit.append({'name': el['name'], 'surname': el['surname'], 'visited': False})

count = 0
while True:
    c = 0
    max_visits = [{'name': to_visit[c]['name'], 'surname': to_visit[c]['surname']}, 0]
    while c < len(to_visit):
        visited = to_visit
        start = visited[0]
        dfs(start)
        if len(list(filter(lambda x: x is True, [el['visited'] for el in visited]))) > max_visits[1]:
            max_visits = [{'name': visited[c]['name'], 'surname': visited[c]['surname']},
                          len(list(filter(lambda x: x is True, [el['visited'] for el in visited])))]
        visited.insert(0, visited.pop(c))
        c += 1
    list_to_invite.append(max_visits)

    visited = []
    for el in read_data:
        visited.append({'name': el['name'], 'surname': el['surname'], 'visited': False})
    for el in list_to_invite:
        visited.insert(0, visited.pop(visited.index(list(filter(lambda x: x['name'] == el[0]['name']
                                                                and x['surname'] == el[0]['surname'], visited))[0])))
        start = visited[0]
        dfs(start)
    to_visit = list(filter(lambda x: x['visited'] is False, visited))
    if not to_visit:
        break
        
print('\n\n2-е задание. \nМинимальное количество людей, которым нужно отправить приглашение, чтобы пригласить всех: ')
for el in list_to_invite:
    print(el[0]['name'], el[0]['surname'])

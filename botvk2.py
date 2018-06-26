import vk_api
import json

filename = "posts.txt"
myfile = open(filename, mode='w', encoding='ascii')

vk = vk_api.VkApi(login='+79781250053', password='omnamahshivaya')
vk.auth()

idgroupsfile = open('idgroups.txt', mode='w')
zapros = input('Введите запрос для поиска групп:')
groups  = vk.method('groups.search', {"q": zapros, 'count': 10})#собираем группы по нужному запросу
idgroups = groups['items']
json.dump(groups, idgroupsfile)

print(groups['count'])
print(idgroups)

for idgroups in idgroups:
    print("Id группы:" + str(idgroups['id']))
    print("Название группы:" + str(idgroups['name']))
    print('________________________________________')

x = input('введите айди группы:')
x = ("-" + x)
q = input('введите ключевое слово:')
kol = input('введите требуемое количество постов:')
wall = vk.method('wall.search', {"owner_id": x, "query": q, "count": kol})#собираем посты по нужному запросу в нужном количестве
json.dump(wall, myfile)
myfile.close()

myfile = open(filename, mode='r', encoding='ascii')
my_posts = json.load(myfile)


rez = open("rez.txt", mode='w', encoding='utf-8') #выводим результаты в файл
ntext = my_posts['items']
for ntext in ntext:
    print("Пост:" + ntext['text'], file=rez)
    print('___________', '\n', '\n', file=rez)




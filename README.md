# Greek civilization
## Описание
Это многопользовательская онлайн-игра, в которой ваша задача состоит в том, что бы превратить маленькую греческую деревню в огромный город, создать мощную армию и покорить соседние города. 


В игре есть три типа ресурсов: дерево, камень и серебро. А города имеют шесть зданий: ферма, склад, лесопилка, каменоломня, рудник, стена. Ферма влияет на максимаольное кол-во жителей ващего города. Улучшать ферму важно(!), потому что каждое улучшение, каждый созданный юнит требует какое-то количетсво населения. Лесопилка, каменоломня, рудник при улучшении производят быстре продукт. Стена даёт бонус при обороне города от нападения другого игрока. Склад ограничивает хранимые ресурсы. Хотите хранить больше? - Улучшайте склад! Так же в складе есть тайник, что позволяет сохранять часть ресурсов при грабеже. 

### Запуск игры
```shell
python client.py start
```
Можно подключаться к определённому серверу, тогада:

```shell
python client.py start -h HOST -p PORT
```
После этого вам надо либо войти в уже существующий игровой аккаут:
```shell
> sign_in -l LOGIN -p PASSWORD
```
Либо содать:
```shell
> sign_up -l LOGIN -p PASSWORD
```
### Игровой процесс
Вы находитесь в опредлённом своём городе. Чтобы переместиться из одного своего в другой, есть соответсвующая команда:
```shell
> change_city -n NAME
```
Все возможные команды вы можете увидеть написав:
```shell
> help
```
Остановимся, на парочке из них:
1) Улучшение здания:
```shell
> update_building -t {Farm,Warehouse,Sawmill,Quarry,Mine,Wall}
```
2) Создание юнитов:
```shell
> create_unit -t {Swordman,Slinger,Archer,Horseman,Chariot,Catapult} [-c COUNT]
```
3) Основание нового города:
```shell
> create_city -n NAME
```
4) Переименование города:
```shell
> rename_city -nn NEW_NAME
```
5) Атака:
```shell
> send_army -pn PLAYER_NAME -cn CITY_NAME -a ARMY
```
Её особенность заключается в сложном формате ввода армии, а именно ARMY должна иметь такой вид: Swordman_Slinger_Archer_Horseman_Chariot_Catapult , где под вместо названия каждого типа необходимо написать, сколько юнитов этого типа из вашей городской армии отправить на противника.

### Запуск сервера
```shell
python server.py
```
Можно поднимать сервер по определенному хосту:
```shell
python server.py -h HOST -p PORT
```

# Постим комиксы в VK
* Скрипт скачивает рандомный комикс с сайта https://xkcd.com/  и постит его
в вашу группу.

### Как установить 
* Должен быть установлен `python3`. Затем используйте `pip`(или `pip3`, 
 если есть конфликт с `Python2`) для установки зависимостей: 
 ```bash
 pip install -r requirements.txt
 ```
 * Для изоляции проекта рекомендуется использовать 
 [virtualenv/venv](https://docs.python.org/3/library/venv.html)
 * Чтобы получить доступ к API VK, необходимо:
    * Узнать id вашей группы ([узнать его можно здесь](http://regvk.com/id/))
    * Получить access_token:
        * Создайте приложение vk. Создать приложение можно в разделе 
        [**Мои приложения**](https://vk.com/apps?act=manage). В качестве типа
         приложения следует указать **standalone**
        * В настройках приложения скопируйте **client_id** и поместите в ссылку:
        https://oauth.vk.com/authorize?client_id=**client_id**&scope=photos,groups,
        wall,offline&response_type=token
        * Вставьте полученную ссылку в адресную строку браузера и перейдите по
        ней 
        * Вы получите access_token — строку наподобие
         533bacf01e1165b57531ad114461ae8736d6506a3. Она появится в адресной
         строке, подписанная как access_token
 * Создайте файл `.env` в одной директории со скриптом
 * Запишите в него id вашей группы и access_token:
 ```txt
 GROUP_ID='12345'
 ACCESS_TOKEN='your_access_token'
  ```
### Как запустить
```bash
python3 main.py
```
 
 ### Цель проекта
 Код написать в образовательных целях на онлайн-курсе для веб-разработчиков 
 [dvmn.org](dvmn.org)
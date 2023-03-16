<h4>https://reqres.in/ - Открытое API</h4>

Необходимо на Python + PyTest написать тестовый фреймворк, где реализовать следующие пункты:
1) Написать позитивные и негативные API тесты, которые представлены на главной странице как образец
2) Написать WEB тесты с главной страницы + добавить проверку, что при нажатии на кнопку отправки образца запроса, получаемый результат (тело ответа и статус код) такой же как и через API запрос
3) Все тесты параметризировать и добавить фикстуры
4) Добавить возможность масштабировать проект (К примеру: если в WEB - добавится новая страница, а в API добавится новая версия API. То в таком случае добавляется новый класс и не нарушается текущая реализация)
<hr>

<h5>test_api.py</h5>

<table>
<tr><th>Тест</th><th>Ожидаемый результат</th><th>Фактический результат</th></tr>
<tr><td>test_get_user</td><td>status_code == 200</td><td>passed</td></tr>
<tr><td>test_create_user</td><td>status_code == 201</td><td>passed</td></tr>
<tr><td>test_update_user</td><td>status_code == 200</td><td>passed</td></tr>
<tr><td>test_delete_user</td><td>status_code == 204</td><td>passed</td></tr>
<tr><td>test_create_user_with_empty_name</td><td>status_code == 400</td><td>FAILED (status_code == 201)</td></tr>
<tr><td>test_get_user_with_invalid_id</td><td>status_code == 404</td><td>passed</td></tr>
<tr><td>test_update_user_with_empty_name</td><td>status_code == 400</td><td>FAILED (status_code == 200)</td></tr>
<tr><td>test_create_user_with_invalid_email</td><td>status_code == 400</td><td>FAILED (status_code == 201)</td></tr>
</table>
<hr>

<h5>test_web.py</h5>

<table>
<tr><th>Тест</th><th>Ожидаемый результат</th><th>Фактический результат</th></tr>
<tr><td>test_post_request</td><td>status_code == 201</td><td>passed</td></tr>
<tr><td>test_web_request</td><td>status_code == 201</td><td>passed</td></tr>
<tr><td>test_compare_results</td><td>status_code == 201, тело ответа должно совпадать с телом ответа API запроса</td><td>FAILED (отличаются id и время создания)</td></tr>
</table>

from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_login():
    login = fake.text(max_nb_chars=7) + str(fake.random_int(0, 999))
    return login


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_firstname():
    first_name = fakeRU.first_name()
    return first_name


def validate_order_structure(order):
    """
    Проверяет полную структуру заказа включая типы данных
    """
    # Ожидаемые поля заказа
    expected_fields = ['id', 'firstName', 'lastName', 'address', 'metroStation',
                      'phone', 'rentTime', 'deliveryDate', 'track', 'color']
    
    # Проверяем наличие всех полей
    missing_fields = [field for field in expected_fields if field not in order]
    
    assert not missing_fields, f"В заказе отсутствуют поля: {', '.join(missing_fields)}"
    
    # Проверяем типы данных обязательных полей
    # Поля которые должны быть числами (могут быть None)
    assert order['id'] is None or isinstance(order['id'], int), "Поле 'id' должно быть числом или None"
    assert order['track'] is None or isinstance(order['track'], int), "Поле 'track' должно быть числом или None"
    assert order['rentTime'] is None or isinstance(order['rentTime'], int), "Поле 'rentTime' должно быть числом или None"
    
    # Поля которые должны быть строками (могут быть None)
    assert order['firstName'] is None or isinstance(order['firstName'], str), "Поле 'firstName' должно быть строкой или None"
    assert order['lastName'] is None or isinstance(order['lastName'], str), "Поле 'lastName' должно быть строкой или None"
    assert order['address'] is None or isinstance(order['address'], str), "Поле 'address' должно быть строкой или None"
    assert order['phone'] is None or isinstance(order['phone'], str), "Поле 'phone' должно быть строкой или None"
    assert order['metroStation'] is None or isinstance(order['metroStation'], str), "Поле 'metroStation' должно быть строкой или None"
    assert order['deliveryDate'] is None or isinstance(order['deliveryDate'], str), "Поле 'deliveryDate' должно быть строкой или None"
    
    # Поле color должно быть списком (может быть None)
    assert order['color'] is None or isinstance(order['color'], list), "Поле 'color' должно быть списком или None"
    
    return True


def get_expected_order_fields():
    """
    Возвращает список ожидаемых полей заказа
    """
    return ['id', 'firstName', 'lastName', 'address', 'metroStation', 
            'phone', 'rentTime', 'deliveryDate', 'track', 'color']


def get_first_order_if_exists(orders_list):
    """
    Безопасно возвращает первый заказ из списка если он существует
    """
    return orders_list[0] if orders_list and len(orders_list) > 0 else None
class ApiResponseMessages:
    """Класс для хранения всех текстовых сообщений от API"""
    
    # Сообщения для курьеров - создание
    LOGIN_ALREADY_EXISTS = 'Этот логин уже используется. Попробуйте другой.'
    NOT_ENOUGH_DATA_FOR_CREATE = 'Недостаточно данных для создания учетной записи'
    
    # Сообщения для курьеров - логин
    NOT_ENOUGH_DATA_FOR_LOGIN = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    
    # Сообщения для заказов
    ORDER_NOT_FOUND = 'Заказ не найден'
    NO_VALID_COURIER = 'Курьер с таким id не найден'
    NOT_ENOUGH_DATA_FOR_ORDER = 'Недостаточно данных для создания заказа'
    
    # Успешные операции
    CREATED_SUCCESSFULLY = 'Пользователь успешно создан'
    LOGIN_SUCCESSFULLY = 'Вход выполнен успешно'
    ORDER_CREATED_SUCCESSFULLY = 'Заказ успешно создан'


class Data:
    # Валидные тестовые данные для курьеров
    valid_login = 'Petrovcky12'
    valid_password = '987654321pass'
    valid_firstname = 'Serj'
    
    # Тестовые данные для создания курьеров
    valid_courier_data = {
        'login': 'Petrovcky', 
        'password': '987654321pass', 
        'firstName': 'Serg'
    }
    
    # Используем класс сообщений
    Messages = ApiResponseMessages


class OrderData:
    # Тестовые данные для заказов
    
    order_data_grey_1 = {
        'firstName': 'Софа',
        'lastName': 'Васильева',
        'address': 'Новиградский проспект, 16',
        'metroStation': 8,
        'phone': '+79853473120',
        'rentTime': 3,
        'deliveryDate': '2024-10-20',
        'comment': 'синий забор',
        'color': ['GREY']
    }

    order_data_black_2 = {
        'firstName': 'Петро',
        'lastName': 'Вайнштейн',
        'address': 'Туссент, улица Яблоневая',
        'metroStation': 10,
        'phone': '+76072861439',
        'rentTime': 7,
        'deliveryDate': '2024-10-19',
        'comment': 'не опаздывать',
        'color': ['BLACK']
    }

    order_data_two_colors_3 = {
        'firstName': 'Ксения',
        'lastName': 'Фазеева',
        'address': 'Шалфей и Розмарин',
        'metroStation': 15,
        'phone': '+73457398129',
        'rentTime': 1,
        'deliveryDate': '2024-10-30',
        'comment': 'проверьте исправность',
        'color': ['BLACK', 'GREY']
    }

    order_data_no_colors_4 = {
        'firstName': 'Иван',
        'lastName': 'Корпут',
        'address': 'Замок Цинтры',
        'metroStation': 20,
        'phone': '+79836517357',
        'rentTime': 2,
        'deliveryDate': '2024-10-20',
        'comment': 'безумно можно быть первым',
        'color': []
    }
    
    # Список всех тестовых заказов для параметризации
    all_order_data = [
        order_data_grey_1,
        order_data_black_2, 
        order_data_two_colors_3,
        order_data_no_colors_4
    ]
from requests import Session

'''Переопределили класс session под свои нужды и задали там параметры'''

class TestSession(Session):
    # чтобы не выскакивала ошибка тк в классе с названием Тест нет по факту тестов или переименовывать класс
    __test__ = False

    def __init__(self):
        # инициализатор session в классе
        super().__init__()
        # self.base_url = base_url

    def request(self, method, path, *args, **kwargs):
        joined_url = f'{self.base_url}{path}'
        return super().request(method, joined_url, *args, **kwargs)

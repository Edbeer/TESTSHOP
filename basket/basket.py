

class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited or overrided, as necessary
    """
    def __init__(self, request):
        self.session = request.session
        """
        Проверка, имеет ли пользвователь сессиию
        """
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            """
            Создание новой сессии для пользователя,
            который не имеет сессию (никогда не заходил на сайт)
            """
            basket = self.session['skey'] = {}
        self.basket = basket

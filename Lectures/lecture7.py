class UserNotFoundError(KeyError):
    pass


class DataStore:
    def __init__(self):
        self._store = {}

    def get_user_email(self, user_id):
        try:
            email = self._store[user_id]
        except KeyError as e:
            raise UserNotFoundError("User ID not found") from e
        return email

    def set_user_email(self, user_id, user_email):
        self._store[user_id] = user_email


def get_value_from_list(index, default=None):
    """ Metod som returnerar ett default-värde om inte indexet vi letar efter finns"""
    my_list = [1, 2, 3]
    try:
        x = my_list[index]
    except IndexError:
        x = default

    return x


def check_input(data):
    if data == 'x':
        print("Doing X!")
    elif data == 'y':
        print("Doing Y!")
    else:
        assert False, "This should never happen! Email me if you encounter this in the wild!"


"""
def update_price(user, product_id, new_price):
    # Absolut inte! Detta är fel!
    assert user.is_admin(), "Must have admin priviliges to change prices!"
    assert store.product_exists(product_id), "Unknown product ID"

    store.update_price(product_id, new_price)
"""


def check_password(password):
    import hashlib
    # Saltning används för att förhindra användadet av förberäknade tabeller (Rainbow Tables)
    # För att använda salt så behöver man helt enkelt lägga på en extra textsnutt på lösenordet. Samma snutt
    # när man producerar hashen som när man jämför den med angivet lösenord.
    #                                  # Salt                    # Lösenordet
    hashed_password = hashlib.sha256(('AS98h3kjrn)FHAysbnfasf' + password).encode()).hexdigest()

    return hashed_password == '4cecba88296aaf63c2f3ea660b79272b152297161bd42799e5fd88719538b480'  # Hej123 i hash


if __name__ == '__main__':
    """
    ds = DataStore()
    ds.set_user_email('1', 'admin@kyh.se')
    ds.set_user_email('15', 'andreas.nilssonstrom@kyh.se')

    print(ds.get_user_email('1'))
    print(ds.get_user_email('15'))
    print(ds.get_user_email('5'))
    """

    # check_input('x')
    # check_input('y')
    # check_input('z')

    print(check_password("Hej123"))  # Ska bli true
    print(check_password("hej123"))  # Ska bli false

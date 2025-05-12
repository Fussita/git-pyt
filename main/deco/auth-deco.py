
def require_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("User is not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_authentication
def get_secret_data(user):
    return "Secret Data"

class User:
    def __init__(self, authenticated):
        self.is_authenticated = authenticated

authenticated_user = User(authenticated=True)
non_authenticated_user = User(authenticated=False)
print(get_secret_data(authenticated_user))

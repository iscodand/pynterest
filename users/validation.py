from users.models.user import User


class Validation():
    
    def validate_password(password: str, field_name: str, error_list: dict) -> None:
        if ' ' in password:
            error_list[str(field_name)] = 'Password must not contain spaces!'
        if len(password) < 8:
            error_list[str(field_name)] = 'Password lenght must be higher than 8 digits!'

    def validate_unique_username(username: str, field_name: str, error_list: dict):
        if User.objects.filter(username=username).exists():
            error_list[str(field_name)] = 'Username already in use! Change and try again.'

    def validate_unique_email(email: str, field_name: str, error_list: dict):
        if User.objects.filter(email=email).exists():
            error_list[str(field_name)] = 'E-mail already in use! Change and try again.'
            
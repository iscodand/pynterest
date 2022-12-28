class Validation():
    
    def validate_password(password: str, field_name: str, error_list: dict) -> None:
        if ' ' in password:
            error_list[str(field_name)] = 'Password must not contain spaces!'
        if len(password) < 8:
            error_list[str(field_name)] = 'Password lenght must be higher than 8 digits!'
from django.core.exceptions import ValidationError

def validate_content(value):
    if value=="":
        raise ValidationError('Content can not be empty')
    return value
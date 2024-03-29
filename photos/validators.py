from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateFileMaxSizeInMb:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes():
            raise ValidationError(self.__get_exception_message())

    def __megabytes_to_bytes(self):
        return self.max_size * 1024 * 1024

    def __get_exception_message(self):
        return f"Max file size is {self.max_size:.02f} MB."


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size


class FileSizeValidator:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        if value.size > self.max_file_size:
            raise ValidationError(f"The size of the file should be less that {self.max_file_size} ")


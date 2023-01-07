from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def get_values(cls):
        return [x.value for x in cls]

    @classmethod
    def get_keys(cls):
        return [x.name for x in cls]

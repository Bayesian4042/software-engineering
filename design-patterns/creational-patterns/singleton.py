class ClassicSingleton:
    __instance = None

    @staticmethod
    def getInstance():
        if ClassicSingleton.__instance == None:
            ClassicSingleton()
        return ClassicSingleton.__instance

    def __init__(self):
        raise Exception("This class is a singleton!")

    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls.__new__(cls)

        return cls.__instance

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass
        
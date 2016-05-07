class MockedClass:

    def __init__(self):
        pass

    @classmethod
    def mocked_class_method(a, b, c, d=10, *args, **kwargs):
        """This is a mocked class method"""
        pass

    def mocked_instance_method(self, a, b, c, d=10, *args, **kwargs):
        """This is a mocked instance method"""
        pass


def mocked_builtin_function(a, b, c):
    """This is a mocked builtin function"""
    pass

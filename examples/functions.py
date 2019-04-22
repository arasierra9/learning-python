"""
Ejemplos de funciones
	* python == 3.7


Ref #: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
Ref #: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
"""


def my_func() -> None:
	print("Hello Kitty!")


my_func() # Hello Kitty!


def my_func() -> int:
	return 1


a = my_func()    # a = 1
print(my_func()) # 1


def args_func(a, b, *args) -> None:
	print(a, b, args)


args_func(1, 2, 3, 4)     # 1 2 (3, 4)
args_func(1, 2, *[3, 4])  # 1 2 (3, 4)


def kwargs_func(a=1, b=2, **kwargs) -> None:
	print(a, b, kwargs)


kwargs_func(1, 2, c=3, d=4)          # 1 2 {'c': 3, 'd': 4}
kwargs_func(1, 2, **dict(c=3, d=4))  # 1 2 {'c': 3, 'd': 4}
kwargs_func(b=2, c=3, d=4)           # 1 2 {'c': 3, 'd': 4}


def mix_func(a, b, *args, c=3, d=4, **kwargs) -> None:
	print(a, b, args, c, d, kwargs)


mix_func(1, 2, 3, 4, 5)                    # 1 2 (3, 4, 5) 3 4 {}
mix_func(1, 2, 3, c=4, d=5)                # 1 2 (3,) 4 5 {}
mix_func(*[1,2,3], **dict(c=4, d=5, e=6))  # 1 2 (3,) 4 5 {'e': 6}



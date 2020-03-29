# A look at dunders beyond __init__
# https://www.geeksforgeeks.org/dunder-magic-methods-python/
# https://rszalski.github.io/magicmethods/


class MyString:
    """A stupid custom string class"""
    def __init__(self, string):
        self.string = string


if __name__ == '__main__':
    some_string = MyString('hey')
    print(MyString)

# Why does Python main work that way?
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

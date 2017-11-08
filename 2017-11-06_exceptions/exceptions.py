def add_two(a, b):
    try:
        return a + b

    except TypeError:
        try:
            return int(a) + int(b)
        except ValueError:
            return float(a) + float(b)

    except ValueError:
        return str(a) + str(b)

    except Exception:
        raise MyCustomException('We could not handle the exception')



class MyCustomException(Exception):
    pass


print(add_two(1, 1))
print(add_two(1.1, 2.0))
print(add_two(1, '5'))
print(add_two(1.1, '2.0'))
print(add_two('1', 'eleven'))

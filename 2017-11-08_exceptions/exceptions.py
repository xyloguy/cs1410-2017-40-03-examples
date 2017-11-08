def calculate_mpg(miles, gallons):
    try:
        return '%s / %s = %s' % \
               (miles, gallons, float(miles)/float(gallons))
    except TypeError as e:
        return 'miles: ' + str(miles) + \
               ', gallons: ' + str(gallons) + \
               ', Error: ' + str(e)
    except ValueError as e:
        return 'miles: ' + str(miles) + \
               ', gallons: ' + str(gallons) + \
               ', Error: ' + str(e)
    except ZeroDivisionError:
        return '%s / %s = 0' % (miles, gallons)


if __name__ == '__main__':
    cases = [
        (300, 10),
        (278.73, 9.67),
        (300, '10'),
        (300, 0),
        ('300', '0'),
        ('300', 'eleven'),
        ([100,100], [10,10]),
        (0, 300),
        (2**64, 2**32),
    ]

    for miles, gallons in cases:
        print(calculate_mpg(miles, gallons))

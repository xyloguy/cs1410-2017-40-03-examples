import marker

def main():
    m = marker.Marker()
    for i in range(10):
        m.write()
    print(m.addInk(1)) #1
    print(m.addInk('1')) #1
    print(m.addInk(1.2)) #1
    print(m.addInk('1.2')) #1
    print(m.addInk('twelve')) #0
    print(m.addInk(100)) #6


if __name__ == '__main__':
    main()

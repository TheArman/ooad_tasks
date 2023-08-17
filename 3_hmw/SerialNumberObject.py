class SerialNumberedObject:
    count = 0

    def __init__(self):
        SerialNumberedObject.count += 1
        self.current_value = SerialNumberedObject.count

    def get_serial_number(self):
        return self.current_value

    def __str__(self):
        return f'I\'m object number {self.current_value}'

    def __repr__(self):
        return self.__str__()


def main():
    ls = [SerialNumberedObject() for _ in range(3)]
    # ls = []
    # obj1 = SerialNumberedObject()
    # obj2 = SerialNumberedObject()
    # obj3 = SerialNumberedObject()
    # ls.append(obj1)
    # ls.append(obj2)
    # ls.append(obj3)

    print(*ls, sep='\n')


main()

glob1 = 1
glob2 = 2

def colors():
    name = 'Ivan'
    glob2 = 'local'

    def print_one():
        one = 'one'
        nonlocal name
        print(name, one, glob1)
        name = 'Vano'
        
    def print_two():
        two = 'two'
        print(name, two, glob2)

    print_one()
    print_two()


colors()

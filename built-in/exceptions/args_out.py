class E(Exception):
    def __str__(self):
        return 'representation E class'

if __name__ == "__main__":
    try:
        raise E('smap')
    except E as e:
        print(e, e.args)

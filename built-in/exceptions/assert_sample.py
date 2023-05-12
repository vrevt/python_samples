if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, 10):
            try:
                assert i != j, f'found {i} = {j}'
            except:
                print(f'{i} == {j}')
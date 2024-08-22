import random
import string
import time


def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper


def print_matrix(n: int, mtrx):
    for i in range(n):
        print(mtrx[i])


@time_execution
def brut_sol(a: str, b: str) -> int:
    n = len(a)
    m = len(b)

    dp = [[0 for i in range(m)] for j in range(n)]

    res = 1
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == 0:
                continue
            for new_i in range(i + 1, n):
                for new_j in range(j + 1, m):
                    if a[new_i] == b[new_j]:
                        dp[new_i][new_j] = max(dp[new_i][new_j], dp[i][j] + 1)
                    res = max(res, dp[new_i][new_j])

    return res - 1


@time_execution
def optimal_sol(a: str, b: str) -> int:
    n = len(a)
    m = len(b)

    dp = [[0 for i in range(m)] for j in range(n)]

    res = 0
    dp[0][0] = 1

    for i in range(0, n):
        for j in range(0, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            if a[i] == b[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            res = max(res, dp[i][j])

    # print_matrix(n, dp)
    return res - 1


def make_random_str():
    n = random.randint(100, 300)
    s = "#" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return s


def run_test(test_amount: int):
    test_num = 0
    while test_num < test_amount:
        test_num += 1
        a = make_random_str()
        b = make_random_str()
        brut_res = brut_sol(a, b)
        optimal_res = optimal_sol(a, b)
        if brut_res == optimal_res:
            print("✅", brut_res, optimal_res)
        else:
            print(a, b)
            print(brut_res)
            print(optimal_res)
            break


if __name__ == "__main__":
    run_test(200)

    # optimal_sol("YQ8", "XNEQBS6Q42")

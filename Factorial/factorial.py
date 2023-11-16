import multiprocessing

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def parallel_factorize(numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(factorize, numbers)
    return results

def main():
    numbers = [128, 255, 99999, 10651060]

    # Синхронна версія
    for number in numbers:
        result = factorize(number)
        print(f"Factors of {number}: {result}")

    # Паралельна версія
    parallel_results = parallel_factorize(numbers)
    for number, result in zip(numbers, parallel_results):
        print(f"Factors of {number}: {result}")

if __name__ == "__main__":
    main()
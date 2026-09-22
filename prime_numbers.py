def is_prime(n: int) -> bool:
    """주어진 정수 n이 소수인지 판별하는 함수"""
    if n < 2:
        return False
    # 2부터 n의 제곱근까지 나누어 떨어지는지 확인
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    start = 1
    end = 100

    # 1부터 100 사이의 소수 찾기
    primes = [num for num in range(start, end + 1) if is_prime(num)]

    print(f"{start}부터 {end} 사이의 소수 목록:")
    print(primes)
    print(f"\n총 {len(primes)}개의 소수가 있습니다.")


if __name__ == "__main__":
    main()


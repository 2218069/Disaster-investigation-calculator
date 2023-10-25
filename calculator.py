def calculate(death, worker):
    if worker == 0:
        return "근로자수가 0이므로 연천인율을 계산할 수 없습니다."
    else:
        ratio = (death / worker) * 1000
        return ratio

while True:
    death = int(input("사망자수를 입력하세요 (종료하려면 -1 입력): "))

    if death == -1:
        break

    worker = int(input("근로자수를 입력하세요: "))

    Disaster_rate = calculate(death, worker)

print(f"연천인율은 {Disaster_rate:.2f}입니다.")

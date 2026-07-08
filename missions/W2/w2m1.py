from multiprocessing import Pool
import time


def work_log(work):
    name, duration = work

    print(f"Process {name} waiting {duration} seconds")
    time.sleep(duration)
    print(f"Process {name} Finished.")


if __name__ == "__main__":
    # 작업 목록: (작업 이름, 실행 시간)
    works = [
        ("A", 5),
        ("B", 2),
        ("C", 1),
        ("D", 3)
    ]

    # 동시에 작업할 프로세스 2개 생성
    with Pool(processes=2) as pool:
        pool.map(work_log, works)
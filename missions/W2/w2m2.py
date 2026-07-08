from multiprocessing import Process

def print_continent(continent = "Asia"):
    print(f"The name of continent is : {continent}")

if __name__ == "__main__":
    # 대륙 이름 목록
    continents = ["Africa", "Europe", "America"]

    processes = [Process(target=print_continent)]  # 기본값 Asia
    processes += [Process(target=print_continent, args=(each,)) for each in continents]


    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
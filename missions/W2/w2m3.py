from multiprocessing import Queue

def main():
    colors = ['red', 'green', 'blue', 'black']
    # 큐 생성
    q = Queue()

    #Push
    print('pushing items to queue:')
    for i, color in enumerate(colors):
        q.put((i, color))
        print(f'item no: {i+1} {color}')

    #Pop
    print('popping items from queue:')
    while not q.empty():
        i, color = q.get()
        print(f'item no: {i} {color}')


if __name__ == "__main__":
    main()
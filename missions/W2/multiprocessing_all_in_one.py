import time
import queue
from multiprocessing import current_process, Queue, Process


def work(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:
            break
        else:
            print(task)
            tasks_that_are_done.put(task + ' is done by ' + current_process().name)
            time.sleep(0.5)

def main():
    number_of_tasks = 10
    number_of_processes = 4

    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    for i in range(number_of_tasks):
        tasks_to_accomplish.put(f'Task no {i}')

    for i in range(number_of_processes):
        p = Process(target=work, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start() #새 프로세스

    for p in processes:
        p.join()

    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

if __name__ == "__main__":
    main()
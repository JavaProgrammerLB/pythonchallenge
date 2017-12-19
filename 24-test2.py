from threading import Thread
import queue

num_worker_threads = 10
queue = queue.Queue(maxsize=0)


def process(item):
    print("doing work for %(item)s" % locals())


def worker():
    while True:
        item = queue.get()
        process(item)
        queue.task_done()


for i in range(num_worker_threads):
    thread = Thread(target=worker)
    thread.daemon = True
    thread.start()

for item in range(10):
    queue.put(item)

queue.join()

print("finished")

import threading

def foo(a, b=30):
    for i in range(b):
        print(i,a)

if __name__ == "__main__":
    t1 = threading.Thread(target=foo, args=('a'), kwargs={'b':40})
    t2 = threading.Thread(target=foo, args=('b'))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('done')

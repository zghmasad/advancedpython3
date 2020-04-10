# Using a pipe to communicate between two processes

from multiprocessing import Process, Pipe


def worker(conn):
    conn.send(['ali', 'sayfi'])
    conn.close()


if __name__ == '__main__':
    main_connection, worker_connection = Pipe()
    p = Process(target=worker, args=[worker_connection])
    p.start()
    print(main_connection.recv())
    main_connection.close()

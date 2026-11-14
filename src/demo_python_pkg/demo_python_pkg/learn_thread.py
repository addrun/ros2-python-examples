# SPDX-License-Identifier: Apache-2.0
"""Three offline worker threads calling the same result callback."""
import threading

def count_words(name, text, callback):
    callback(name, len(text.split()))

def print_result(name, count):
    print(f'{name}: {count} words')

def main():
    samples = [('nodes', 'ROS nodes exchange messages'),
               ('topics', 'Publishers and subscribers communicate through topics'),
               ('callbacks', 'An executor dispatches callbacks')]
    workers = [threading.Thread(target=count_words, args=(name, text, print_result))
               for name, text in samples]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

if __name__ == '__main__':
    main()

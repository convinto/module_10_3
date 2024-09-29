import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance= 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            sum_log = randint(50, 500)
            with self.lock:
                if self.balance <= 500 and self.lock.locked():
                    self.balance = self.balance + sum_log
                    print(f'Пополнение: {sum_log}. Баланс: {self.balance}.')
            sleep(0.001)

# Попытался реализовать блокировку потока методом acquire
    def take(self):
        for i in range(100):
            self.lock.acquire()
            sum_log = randint(50, 500)
            print(f'Запрос на {sum_log}.')
            #self.lock.acquire()
            if self.balance >= sum_log:
                self.balance = self.balance - sum_log
                print(f'Снятие: {sum_log}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонен, недостаточно средств.')
            self.lock.release()
            sleep(0.001)


# Вариант с with
    # def take(self):
    #     for i in range(100):
    #         sum_log = randint(50, 500)
    #         print(f'Запрос на {sum_log}.')
    #         with self.lock:
    #             if self.balance >= sum_log:
    #                 self.balance = self.balance - sum_log
    #                 print(f'Снятие: {sum_log}. Баланс: {self.balance}.')
    #             else:
    #                 print(f'Запрос отклонен, недостаточно средств.')
    #         sleep(0.001)



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
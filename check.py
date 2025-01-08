import random

numlist = [random.randint(0, 100) for _ in range(100)]

checkedlist = [int(i/50) for i in numlist]

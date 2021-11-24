def coroutine():
    while True:
        value = (yield)
        print(value)


routine = coroutine()
next(routine)

routine.send(5)
routine.send(9)
routine.send('Hi')
routine.send(True)

routine.close()

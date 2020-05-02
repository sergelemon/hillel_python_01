def what_is_coro():
    print(f"Starting point")
    value = 2 * (yield)
    print(f"New value x2 = {value}")
    value = 3 * (yield)
    print(f"New value x3 = {value}")

c = what_is_coro()
next(c)
c.send(2)
try:
    c.send(3)
except StopIteration:
     pass
c.close()

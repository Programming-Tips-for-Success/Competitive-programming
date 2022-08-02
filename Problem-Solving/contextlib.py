
# What is the output of the following Python 3 code:
import contextlib
@contextlib.contextmanager
def Program():
    try:
        yield from perform()
    except:
        raise
    else:
        return 0
def perform():
    yield 
def task():
    for n in range(7):
        with Program():
            yield n
            raise StopIteration
for n in task():
    print(n, end=' ')

# StopIteration -> correct output
# 1 2 3 4 5 6
# 0 1 2 3 4 5 6
# RuntimeError


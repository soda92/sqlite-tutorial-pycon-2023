import contextlib


@contextlib.contextmanager
def CD(dir: str):
    import os

    old_dir = os.getcwd()
    os.chdir(dir)
    try:
        yield None
    finally:
        os.chdir(old_dir)


import os

print(os.getcwd())

with CD("C:"):
    print(os.getcwd())

print(os.getcwd())

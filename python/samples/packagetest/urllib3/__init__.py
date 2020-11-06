class SomeThing:
    data = 'you have been duped'

class PoolManager:
    def __init__(self):
        pass

    def request(self, a,b):
        print(a,b)
        return SomeThing()

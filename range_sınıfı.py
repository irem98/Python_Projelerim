class Series(object):
    def __init__(self,low,high):
        self.__low = low
        self.__high = high

    def __iter__(self):
        self.__current = self.__low
        return self

    def __next__(self):
        if self.__current > self.__high:
            raise StopIteration

        self.__current += 1
        return self.__current -1

series = Series(1,5)

for s in series:
    print(s)

# class QueueError(IndexError):  # Choose base class for the new exception.
#     pass

# class Queue:
#     def __init__(self):
#         self.__lista = []

#     def put(self, elem):
#         self.__lista.insert(0, elem)

#     def get(self):
#         if len(self.__lista) > 0:
#             val = self.__lista[-1]
#             del self.__lista[-1]
#             return val
#         else:
#             raise QueueError


# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Queue error")


class A:
    def __init__(self):
        pass
a = A(1)
print(hasattr(a,'A'))
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None


def process_queries(queries):
    q = Queue()
    output = []
    for query in queries:
        if query[0] == 1:
            q.push(query[1])
        elif query[0] == 2:
            popped = q.pop()
            if popped is not None:
                output.append(popped)
    return output


Q = 5
queries = [(1, 2), (1, 3), (2,), (1, 4), (2,)]
result = process_queries(queries)
print(result)
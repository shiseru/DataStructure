def BFS(graph, s):
    queue = []
    queue.append(s)

    while len(queue) != 0:
        v = queue.pop(0)

        for each neighour u of v:
            if u not in queue:
                queue.append(u)

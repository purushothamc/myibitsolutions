def hotel(arrive, depart, K):
    events = [(x, 0) for x in arrive] + [(x, 1) for x in depart]
    events = sorted(events)
    print events
    count = 0
    for event in events:
        if event[1] == 0:
            count += 1
        else:
            count -= 1
        if count > K: return False
    return True
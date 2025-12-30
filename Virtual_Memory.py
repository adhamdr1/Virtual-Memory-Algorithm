def fifo(pages, capacity):
    memory = []
    page_faults = 0
    for p in pages:
        if p not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(p)
            else:
                memory.pop(0)
                memory.append(p)
    return page_faults

def lru(pages, capacity):
    memory = []
    page_faults = 0
    for p in pages:
        if p not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(p)
            else:
                memory.pop(0)
                memory.append(p)
        else:
            memory.remove(p)
            memory.append(p)
    return page_faults

def lfu(pages, capacity):
    memory = []
    freq = {}
    page_faults = 0
    for p in pages:
        freq[p] = freq.get(p, 0) + 1
        
        if p not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(p)
            else:
                least_frequent_page = min(memory, key=lambda x: freq[x])
                memory.remove(least_frequent_page)
                memory.append(p)
    return page_faults

def mfu(pages, capacity):
    memory = []
    freq = {}
    page_faults = 0
    for p in pages:
        freq[p] = freq.get(p, 0) + 1
        
        if p not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(p)
            else:
                most_frequent_page = max(memory, key=lambda x: freq[x])
                memory.remove(most_frequent_page)
                memory.append(p)
    return page_faults

def clock(pages, capacity):
    memory = [None] * capacity
    use_bit = [0] * capacity
    pointer = 0
    page_faults = 0
    
    for p in pages:
        if p in memory:
            use_bit[memory.index(p)] = 1
        else:
            page_faults += 1
            while use_bit[pointer] == 1:
                use_bit[pointer] = 0
                pointer = (pointer + 1) % capacity
            memory[pointer] = p
            use_bit[pointer] = 1
            pointer = (pointer + 1) % capacity
    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 0, 3, 2, 1, 0, 4, 5]
capacity = 3

print("FIFO:", fifo(pages, capacity))
print("LRU:", lru(pages, capacity))
print("LFU:", lfu(pages, capacity))
print("MFU:", mfu(pages, capacity))
print("Clock:", clock(pages, capacity))
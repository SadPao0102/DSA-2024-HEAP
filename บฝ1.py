import heapq

def insert_to_max_heap(heap, values):
    for value in values:
        heapq.heappush(heap, -value)  # ใช้ค่าลบเพื่อให้ heapq ทำงานเป็น Max Heap

def main():
    values = [5, 3, 8, 1, 2, 7, 6, 4]
    max_heap = []
    insert_to_max_heap(max_heap, values)
    
    # แปลงค่ากลับเป็นบวกเพื่อแสดงค่า Max Heap
    max_heap_result = [-x for x in max_heap]
    print("Max Heap:", max_heap_result)

if __name__ == "__main__":
    main()
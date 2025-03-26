import heapq

def insert_to_max_heap(heap, values):
    for value in values:
        heapq.heappush(heap, -value)  # ใช้ค่าลบเพื่อให้ heapq ทำงานเป็น Max Heap

def remove_max(heap):
    if heap:
        return -heapq.heappop(heap)  # แปลงค่ากลับเป็นบวกเมื่อดึงออก
    return None

def main():
    values = [5, 3, 8, 1, 2, 7, 6, 4]
    max_heap = []
    insert_to_max_heap(max_heap, values)
    
    # แปลงค่ากลับเป็นบวกเพื่อแสดงค่า Max Heap
    max_heap_result = [-x for x in max_heap]
    print("Initial Max Heap:", max_heap_result)
    
    # ลบค่ามากที่สุดออก 3 ครั้ง
    for i in range(3):
        removed = remove_max(max_heap)
        max_heap_result = [-x for x in max_heap]
        print(f"After removing max {i+1}: {removed}, Heap: {max_heap_result}")

if __name__ == "__main__":
    main()

import heapq
from datetime import datetime
import time

class BankCustomer:
    queue_counter = 1  # ตัวนับเลขคิว
    
    def __init__(self, service_type, is_premium=False):
        self.queue_number = BankCustomer.queue_counter
        BankCustomer.queue_counter += 1
        
        self.service_type = service_type
        self.is_premium = is_premium
        self.arrival_time = datetime.now()
        self.priority = self._calculate_priority()

    def _calculate_priority(self):
        priority = {
            'ฝาก-ถอน': 3,
            'ชำระค่าบริการ': 2,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 0
        }
        base_priority = priority.get(self.service_type, 4)
        if self.is_premium:
            base_priority -= 0.5
        return base_priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

class BankQueue:
    def __init__(self):
        self.queue = []
        self.waiting_count = 0

    def add_customer(self, customer):
        heapq.heappush(self.queue, customer)
        self.waiting_count += 1
        print(f"เพิ่มหมายเลขคิว: {customer.queue_number} | บริการ: {customer.service_type} | {'Premium' if customer.is_premium else 'ทั่วไป'}")
        print(f"จำนวนคิวรอ: {self.waiting_count}\n")

    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return None
        
        customer = heapq.heappop(self.queue)
        self.waiting_count -= 1
        wait_time = datetime.now() - customer.arrival_time
        print(f"\nเรียกคิวหมายเลข: {customer.queue_number} | บริการ: {customer.service_type} | เวลารอ: {wait_time.seconds} วินาที")
        print(f"จำนวนคิวที่เหลือ: {self.waiting_count}\n")
        return customer

    def display_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว\n")
            return
        
        print("\nรายการคิวที่รอ:")
        temp_queue = self.queue.copy()
        while temp_queue:
            customer = heapq.heappop(temp_queue)
            print(f"คิวหมายเลข {customer.queue_number} - {customer.service_type}")
        print("-" * 30)

# โปรแกรมหลัก
if __name__ == "__main__":
    bank = BankQueue()
    transactions = ['ฝาก-ถอน', 'ชำระค่าบริการ', 'เปิดบัญชี', 'สินเชื่อ']
    
    while True:
        print("\nเลือกธุรกรรม:")
        for i, txn in enumerate(transactions, 1):
            print(f"{i}. {txn}")
        print("5. เรียกคิวถัดไป")
        print("6. แสดงรายการคิว")
        print("7. ออกจากโปรแกรม")
        
        choice = input("เลือกหมายเลข: ")
        
        if choice in ['1', '2', '3', '4']:
            service_type = transactions[int(choice) - 1]
            is_premium = input("ลูกค้าเป็น Premium หรือไม่ (y/n): ").strip().lower() == 'y'
            customer = BankCustomer(service_type, is_premium)
            bank.add_customer(customer)
        elif choice == '5':
            bank.serve_next_customer()
        elif choice == '6':
            bank.display_queue()
        elif choice == '7':
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่\n")
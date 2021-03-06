# 모각코 9일차
# 큐 문제
# 원형 큐 사용

MAX_SIZE = 10

class Queue:
  # 큐 초기화
  def init(self):
    self.arr = [None]*MAX_SIZE
    self.front = 0
    self.rear = 0

  # 큐 꽉 찼는지 확인
  def is_full(self):
    if (self.rear+1) % MAX_SIZE == self.front:
      return True
    return False
  
  # 큐 비었는지 확인
  def is_empty(self):
    if self.front==self.rear:
      return True
    return False

  def enqueue(self, val):
    if self.is_full():
      print("Queue is full")
      return
    else:
      self.rear = (self.rear + 1) % MAX_SIZE
      self.arr[self.rear] = val

  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
      return
    else:
      self.front = (self.front + 1) % MAX_SIZE
      return self.arr[self.front]

queue = Queue()
queue.init()
id_list=[]

# 입력받기
for _ in range(7):
  id, min = input().split()
  id_list.append(id)
  queue.enqueue(min)

task=0
total=0
start=0
id_num=0
MAX_TIME = 50

while (queue.is_empty()==False):
  next_task = int(queue.dequeue())

  if task+next_task <=MAX_TIME:
    task += next_task
    id_num+=1

  else:
    total += (task +10)
    task = next_task
    
    print(id_list[start:id_num])
    
    start=id_num
    id_num+=1
  
print(id_list[start:id_num])
print(f'총 소요시간 : {total+task}분')
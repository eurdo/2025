class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleCircularLinkedList:
    """雙向循環列表類"""
    def __init__(self):
        self._head = None
        
    @property
    def is_empty(self):
        """
        檢查列表是否為空
        :return: 
        """
        return not self._head
    
    @property
    def length(self):
        """
        鏈表長度
        :return: 
        """
        if self.is_empty:
            return 0
        else:
            cur = self._head.next
            n = 1
            while cur != self._head:
                cur = cur.next
                n += 1
            return n
        
    @property
    def ergodic(self):
        """
        遍歷鏈表
        :return: 
        """
        if self.is_empty:
           raise ValueError("ERROR NULL")
        else:
            cur = self._head.next
            print(self._head.item)
            while cur != self._head:
                print(cur.item)
                cur = cur.next

    def add(self, item):
        """
        頭部添加節點
        :return: 
        """
        node = Node(item)
        if self.is_empty:
            node.next = node
            node.prev = node
            self._head = node
        else:
            node.next = self._head
            node.prev = self._head.prev
            self._head.prev.next = node
            self._head.prev = node
            self._head = node

    def append(self, item):
        """
        尾部添加節點
        :param item:
        :return: 
        """
        if self.is_empty:
            self.add(item)
        else:
            node = Node(item)
            cur = self._head.next
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.prev = cur
            node.next = self._head
            self._head.prev = node

    def insert(self, index, item):
        """
        任意位置插入節點
        :param item: 
        :return: 
        """
        if index == 0:
            self.add(item)
        elif index+1 >= self.length:
            self.append(item)
        else:
            cur = self._head.next
            n = 1
            while cur.next != self._head:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node

    def search(self, item):
        """
        查找節點是否存在
        :return: 
        """
        if self.is_empty:
            return False
        else:
            cur = self._head.next
            if self._head.item == item:
                return True
            else:
                while cur != self._head:
                    if cur.item == item:
                        return True
                    else:
                        cur = cur.next
                return False
            
    def delete(self, item):
        """
        刪除指定值的節點
        :param item: 
        :return: 
        """
        if self.is_empty:
            raise ValueError("ERROR NULL")
        else:
            if self._head.item == item:
                if self.length == 1:
                    self._head = None
                else:
                    self._head.prev.next = self._head.next
                    self._head.next.prev = self._head.prev
                    self._head = self._head.next
            cur = self._head.next
            while cur != self._head:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.next
                
if __name__ == "__main__":
    dl = DoubleCircularLinkedList()
    print("空？", dl.is_empty, "長度:", dl.length)

    dl.add(10)
    dl.append(20)
    dl.insert(1, 15)
    print("內容：")
    dl.ergodic
    print("長度:", dl.length)

    print("刪除15")
    dl.delete(15)
    dl.ergodic
    print("長度:", dl.length)
    print("查找20:", dl.search(20))
        

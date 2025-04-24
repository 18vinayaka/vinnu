class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None


    def disp(self):
        if self.head is None:
            print("")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="---->")
                temp=temp.next
            print("None")

    def ins_at_beg(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb

    def ins_at_end(self,data):
        ne=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=ne

    def ins_at_pos(self,data,pos):
        temp=self.head
        np=node(data)
        for i in range(pos):
            temp=temp.next
            np.next=temp.next
        temp.next=np

    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def del_at_end(self):
        temp=self.head.next
        prev=self.head

        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def del_at_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(pos):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        



n1=node(10)
n2=node(20)
n3=node(30)

l1=sll()
l1.head=n1
n1.next=n2
n2.next=n3

l1.disp()

l1.ins_at_beg(5)
l1.disp()

l1.ins_at_end(40)
l1.disp()

l1.ins_at_pos(35,3)
l1.disp()

l1.del_at_beg()
l1.disp()

l1.del_at_end()
l1.disp()


l1.del_at_pos(2)
l1.disp()


#!/usr/bin/env python3

class MyList:
    def __init__(self) -> None:
        self.data = [1,2,3,4,5]

    def __getitem__(self,index):
        return self.data[index]
        
list = MyList()
print(list[2])
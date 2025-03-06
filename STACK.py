class stack:
    def __init__(self ,list):
        self.list = list
    def push(self, data):
        self.data = data
        self.list.append(self.data)
    def pop(self):
        if(self.list == []):
            return "Stack is empty"
        else:
            return self.list.pop()
    def top(self):
        if(self.list == []):
            return "Stack is empty"
        else:
            return self.list[-1]
    def get_min(self):
        if(self.list == []):
            return "Stack is empty"
        m=self.list[0]
        for i in self.list:
            if(i<m):
                m=i
        return m
    def get_max(self):
        if(self.list == []):
            return "Stack is empty"
        m=self.list[0]
        for i in self.list:
            if(i>m):
                m=i
        return m

list = []
s = stack(list)
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Get Min")
    print("5. Get Max")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        s.push(data)
    elif choice == 2:
        print(s.pop())
    elif choice == 3:
        print(s.top())
    elif choice == 4:
        print(s.get_min())
    elif choice == 5:
        print(s.get_max())
    elif choice == 6:
        break
    else:
        print("Invalid choice")

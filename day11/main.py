from typing import List
   

class Monkey:
    def __init__(self, **kwargs):
        self.items = kwargs["items"]
        self.operation = kwargs["operation"]
        self.test = kwargs["test"]
        self.true_throw = kwargs["true_throw"]
        self.false_throw = kwargs["false_throw"]
        self.inspected = 0
        
    def receive_item(self, item):
        self.items.append(item)
        
    def pass_item(self, monkeys, relief_factor):
        item = self.items[0]
        self.items = self.items[1:]
        self.inspected += 1
        item = int(self.operation(item))
        item //= relief_factor
        if self.test(item):
            monkeys[self.true_throw].receive_item(item)
        else:
            monkeys[self.false_throw].receive_item(item)
    
    def pass_items(self, monkeys, relief_factor):
        while self.items:
            self.pass_item(monkeys, relief_factor)
            
    def __repr__(self):
        return str(self.__dict__)

def read_input():

    with open("input") as f:
        lines = f.readlines()

    monkeys: List[Monkey] = []

    worry_mod = 1
    for line in lines:
        split: List[str] = line.strip().split(":")
        line_start = split[0]
        if line_start.startswith("Monkey"):
            current_monkey = {}
        elif line_start == "Starting items":
            current_monkey["items"] = [int(x) for x in split[1].split(",")]
        elif line_start == "Operation":
            if split[1].strip() == "new = old * old":
                current_monkey["operation"] = lambda x: int(x * x) % worry_mod
            else:
                op = split[1].split(" ")
                num = int(op[-1])
                current_monkey["operation"] = lambda x, num=num: int(x * num) % worry_mod
                if op[-2] == "+":
                    current_monkey["operation"] = lambda x, num=num: int(x + num) % worry_mod
        elif line_start == "Test":
            test = split[1].split(" ")
            num = int(test[-1])
            worry_mod *= num
            current_monkey["test"] = lambda x, num=num: x % num == 0
        elif line_start == "If true":
            current_monkey["true_throw"] = int(split[1].split(" ")[-1])
        elif line_start == "If false":
            current_monkey["false_throw"] = int(split[1].split(" ")[-1])
            monkeys.append(Monkey(**current_monkey))    
    
    return monkeys

monkeys = read_input()
for i in range(20):
    for j in range(len(monkeys)):
        monkeys[j].pass_items(monkeys, 3)
        
sorted_monkeys = list(sorted(monkeys, key = lambda x: x.inspected))
print(f"P1: {sorted_monkeys[-1].inspected * sorted_monkeys[-2].inspected}")

monkeys = read_input()
for i in range(10000):
    for j in range(len(monkeys)):
        monkeys[j].pass_items(monkeys, 1)
        
for m in monkeys:
    print(m.inspected)
        
sorted_monkeys = list(sorted(monkeys, key = lambda x: x.inspected))
print(f"P2: {sorted_monkeys[-1].inspected * sorted_monkeys[-2].inspected}")

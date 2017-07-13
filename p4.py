# p4.py

class Turtle:
    color = "GREEN"
    weight = 10
    shell = True
    mouth = "大嘴"

    def climb(self):
        print("我正在很努力的往上爬...")
    def run(self):
        print("我正在飞快的往前跑...")
    def bite(self):
        print("咬死你,咬死你!!")
    def eat(self):
        print("有的吃,真满足^-^")
    def sleep(self):
        print("困了,睡觉了,晚安^-^")
    def display(self):
        print("color:" + str(self.color))
        print("weight:" + str(self.weight))
        print("shell:" + str(self.shell))
        print("mouth:" + self.mouth)
    
tt = Turtle()
tt.display()

# evaluator.py
# Implements and evaluates postfix arithmetic expressions

def evaluate(s):
    list = []
    for i in s:
        if i.isdigit():
            list.append(i)
        else:
            b=float(list.pop())
            a=float(list.pop())

            if i=="+":
                ans=a+b
            elif i=="*":
                ans=a*b
            elif i=="/":
                if b==0:
                    return "math-error"
                ans=a/b
            elif i=="-":
                ans=a-b

            list.append(ans)

    return list.pop()
    

print(evaluate("23+5*6/"))



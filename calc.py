def main():
    x=int(input("x"))
    y=int(input("y"))
    print("%d*%d=%0.3f"%(x,y,mul(x,y)))
def mul(x,y):
    return x*y
if __name__=="main":
    main()
data = list(map(int, input()))

#code

if sum(data[:len(data)//2]) == sum(data[len(data)//2:]) :
    print("LUCKY")
else:
    print("READY")


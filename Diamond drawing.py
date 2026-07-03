def draw_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "/" + " " * (2 * i) + "\\")
    
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "\\" + " " * (2 * i) + "/")

draw_diamond(5)

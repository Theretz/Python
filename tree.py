def tree(height):
    lenght = height * 2 - 1 
    stars = 1 
    for i  in range (height + 1):
        print(("★" * stars).center(lenght))
        stars += 2 
        print("★".center(lenght))

tree(9)
tree(20)
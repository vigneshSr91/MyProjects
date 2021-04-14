# pre-requisite is the sides of the rectangle are parallel to the X and Y axis
if __name__ == '__main__':
    TopX, TopY = map(int,input("Enter Top X,Y coordinate: ").split(','))
    top = (TopX, TopY)
    print(top)
    BottomX, BottomY = map(int,input("Enter Bottom X,Y coordinate: ").split(','))
    bottom = (BottomX, BottomY)
    print(bottom)

    ReferenceX, ReferenceY = map(int,input("Enter Reference X,Y coordinate: ").split(','))
    reference=(ReferenceX, ReferenceY)
    print(reference)

    if(reference[1] <= top[1] and reference[1] >= bottom[1] and reference[0] >= top[0] and reference[0] <= bottom[0]):
        print("Reference point lies within/on the rectangle")
    else:
        print("Reference point lies outside the rectangle")

    
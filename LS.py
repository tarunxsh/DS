def ls(lys, element):  
    for i in range(len(lys)):
        if lys[i] == element:
            print('{} is found on index {}'.format(b,i))
            break
    else:
        print('{} is not found'.format(b))


a=[2,3,1,4,5,7,55,9]
b=55
ls(a,b)


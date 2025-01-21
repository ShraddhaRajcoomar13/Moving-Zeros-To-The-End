def move_zeros(lst):
    p=[i for i in lst if i!=0]
    l=[i for i in lst if i==0]
    lst=p+l
    return lst

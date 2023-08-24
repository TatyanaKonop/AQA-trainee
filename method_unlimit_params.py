def my_method(*data):
    lens = len(data)
    for i in data:
        if type(i) == list:
            for j in range(len(i)-1):
                print(f'{j+1}:{i[j]}', end = ",")
            l = len(i)-1
            print(f'{len(i)}:{i[l]}', end=' ')
        else:
            if lens > 1:
                print(i, end =",")
            else:
                print(i)
        lens = lens - 1
my_method([1,3,5, 'маша',3, 'ukt',1,2,5,'vfif'])



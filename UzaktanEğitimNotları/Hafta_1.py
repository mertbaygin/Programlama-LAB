import random

def get_n_random_numbers(n=10,min=-5,max=5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

dizi = get_n_random_numbers()
# print(dizi)
def my_frequency_with_dict(dizi):
    frequency_dict = {} # dict()= {}
    for item in dizi:
        if(item in frequency_dict):
            frequency_dict[item] = frequency_dict[item] +1
        else:
            frequency_dict[item]=1
    return frequency_dict

#print(my_frequency_with_dict(dizi))
def my_frequency_with_list_of_tuples(liste_1):
    frequency_list = []
    for i in range(len(liste_1)):
        s = False
        for j in range(len(frequency_list)):
            if(liste_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([liste_1[i],1])
    return frequency_list


my_list = [2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_with_list_of_tuples(my_list)



# mode bir listedeki en çok tekrar eden kelime

my_list_1 = get_n_random_numbers(5,-2,2)
my_hist_d =  my_frequency_with_dict(my_list_1)
def my_mode_with_dict(my_hist_d):
    frequency_max = 1
    mode = -1
    for key in  my_hist_d.keys():
        print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode,frequency_max


# mode of a list histogram(a list of tuples)
my_list_1 = get_n_random_numbers(10)
x=my_frequency_with_list_of_tuples(my_list_1)
def my_mode_with_list(x):
    frequency_max = -1
    mode = -1
    for item,frequency in x:
        print(item,frequency)
        if frequency > frequency_max:
            frequency_max = frequency
            mode = item
    return mode,frequency

# Lineer search on list 
my_list_2 = get_n_random_numbers(15,-50,50)
#print(my_list_2)
def my_search(my_list,item_search):
    found = (-1,-1)
    n=len(my_list)
    for indis in range(n):
        if my_list[indis] == item_search:
            found = (my_list[indis],indis)
    return found
#print(my_search(my_list_2,3))

#mean of list
s,t = 0,0
for item in my_list_2:
    s=s+1
    t=t + item
    mean_ = t/s
#print(mean_)
def my_mean(my_list_2):
    s,t = 0,0
    for item in my_list_2:
        s=s+1
        t=t + item
        mean_ = t/s
    return mean_

#sort the list
#bubble short

n = len(my_list_2)
#print(my_list_2)
for i in range(n-1,-1,-1):
    for j in range(0,i):
        if not(my_list_2[j]<my_list_2[j+1]):
            temp=my_list_2[j]
            my_list_2[j]=my_list_2[j+1]
            my_list_2[j+1]=temp
#print(my_list_2)

#Fonskiyon bubble short
def bubbleShort(my_list_2):
    n = len(my_list_2)
    print(my_list_2)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list_2[j]<my_list_2[j+1]):
                temp=my_list_2[j]
                my_list_2[j]=my_list_2[j+1]
                my_list_2[j+1]=temp
    return my_list_2


#binary search on a shorted list
def my_binary_search(my_list_2,item_search):
    found = (-1,-1)
    low = 0
    high = len(my_list_2)-1
    while low<=high:
        mid = (low + high)//2
        if my_list_2[mid]==item_search:
            return my_list_2[mid],mid
        elif my_list_2[mid] > item_search:
            high = mid-1
        else:
            low = mid +1
    return found

#print(my_binary_search(my_list_2,9))

#median of a list

size = int(input('dizi boyutu gir:'))
my_list_3 = get_n_random_numbers(size)
#print("Liste ",my_list_3)

my_list_4 = bubbleShort(my_list_3)
print(my_list_4)
n= len(my_list_4)
if n%2 == 1:
    middle = int(n/2)+1
    median = my_list_4[middle]
    #print(median)
else:
    middle_1 = my_list_4[int(n/2)]
    middle_2 = my_list_4[int(n/2)+1]
    median= (middle_1 + middle_2)/2
    #print(median)

def my_median(x):
    my_list_2 = bubbleShort(x)
    #print(my_list_2)
    n= len(my_list_2)
    if n%2 == 1:
        middle = int(n/2)+1
        median = my_list_2[middle]
        #print(median)
    else:
        middle_1 = my_list_2[int(n/2)]
        middle_2 = my_list_2[int(n/2)+1]
        median= (middle_1+middle_2)/2
        #print(median)
    return int(median)


new_list = get_n_random_numbers(6,-10,10)
print(my_median(new_list))
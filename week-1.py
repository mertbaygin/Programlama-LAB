# verilen sayının üssünü bulan python kodu
def power(a,b):
  if b==0:
    return 1
  elif b==1:
    return a
  else:
    if b%2==0:
      return power(a*a,b//2)
    else:
      return power(a*a,b//2)*a
    
*************************************************
# verilen bir sayı dizisin de ardışık sayılar arasında en büyük olanı bulma -1

liste=[4,-3,5,-2,-1,2,6,-2]
max_=0
for i in range(8):
  for j in range(i,8):
    t=0
    for k in range(i,j):
      t=t+liste[k]
    if max_<t:
      max_=t
      ibas,json=i,j
print(max_,ibas,json)

***************************************************  -2
def max_of_two(a,b):
    if(a>b):
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))


def my_f_(list_1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(list_1)
    if (n==1):
        return list_1[0]
    left_i=0
    left_j=n//2
    right_i=n//2
    right_j=n
    left_sum=my_f_(list_1[left_i:left_j])
    right_sum=my_f_(list_1[right_i:right_j])
    temp_left_sum=0
    t=0
    for k in range(left_j-1,left_i-1,-1):
        t=t+list_1[k]
        if(t>temp_left_sum):
            temp_left_sum=t
    temp_right_sum=0
    t=0
    for m in range(right_i,right_j):
        t=t+list_1[m]
        if(t>temp_right_sum):
            temp_right_sum=t
    center_sum=temp_left_sum+temp_right_sum
    return max_of_three(left_sum,right_sum,center_sum)

    

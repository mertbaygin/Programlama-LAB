#Kabarcık sıralama algoritmasının ortalama ve en kötü durumdaki çalışma zamanı O(n**2)
#Ortalam ve en kötü durumlarda yapacağı karşılaştırma sayısı (n**2/2)
def buble_sort():

    liste = [12,4,124,5,3,0,-12,24,9,14]

    for i in range(len(liste)):
        for j in range(len(liste)-1):
            print(i,j)
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j]=liste[j+1]
                liste[j+1] = temp

    return liste

print(buble_sort())




# O notasyonu diğer yerleştirmeli sıralamalardan farklı olacaktır, normal durumlarda ve en kötü durumda O(nlogn)'dir
#Algoritmanın yapacağı karşılaştırma sayısı her zaman C=n(logn-loge-+0,5) olacaktır.

array =[3,0,1,8,7,2,5,4,9,6]
def yerDegis(x,y):
    temp =array[x]
    array[x]=array[y]
    array[y]=temp

for i in range(9,1,-1):
    j=0
    while (j<i):
        if(array[j] > array[j+1]):
            yerDegis(j,j+1)
        j+=1


# Dizinin ikinci elemanından başlanarak kayıtlar sırayla kontrol edilir.
# Bir önceki kayıt o anki kayıttan büyükse bu iki elemanın yerleri değiştirilir.
# Normal ve en kötü durumda O(n^2)dir
# Her durumda yapacağı karşılaştırma sayısı C=n(n-1)/2



array =[3,0,1,8,7,2,5,4,9,6]
def yerDegis(x,y):
    temp =array[x]
    array[x]=array[y]
    array[y]=temp


for i in range(1,len(array)):
    j=i
    while (j>0):
        if(array[j] < array[j-1]):
            yerDegis(j,j-1)
        else:
            break
        j=j-1

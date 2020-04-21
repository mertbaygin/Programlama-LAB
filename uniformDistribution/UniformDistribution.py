# MERT BAYGIN 180401104
#Github Link :https://github.com/mertbaygin/Programlama-LAB
""""
Uniform Distribution / Tekdüze Dağılım
Bir rasgele değişken için olası değerlerin ortaya çıkma olasılıkları eşitse bu rasgele değişken tekdüze dağılıma eşittir denir.
Özet olarak Matematiksel olarak rastgele üretilen sayıların belirli bir düzen içerisinde olması durumudur.

# Örneğin bir resimdeki histogramın çıkarılması sonucu bütün resmin verilen aralıktaki renk kodlarından aynı miktarda alması
veya bir ağ iletişimi sırasında sinyal üzerinde oluşan gürültünün sinyalin aynı aralığında aynı miktarda uygulanması gibi.

Bu dağılımın fonksiyonu ;
       
                                               
        l    1/(b-a) ,  a<=x<=b,           
        l                                          
f(x)=   l
        l                                         
        l    0       , x<a veya x>b  
        l                                        
                                                    
""""


import sympy as sym
from sympy import Symbol, pprint, Piecewise
import sympy.plotting as syp
import matplotlib.pyplot as plt

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
ud = 1 /(b-a)


pprint(ud)


#bd = int(input('Başlangıç değeri giriniz'))
#bitisd = int(input('Bitiş değeri giriniz'))

def uniformDis(bd, bitisd):
    syp.plot(Piecewise((0, (x < bd) | (x > bitisd)), (ud.subs({a: bd, b: bitisd}), (x >= bd) & 
        (x <= bitisd))), (x, -15, 15), title="uniformDistribution")


from numpy import random
import seaborn as sns
#Seaborn, Matplotlib kütüphanesine yüksek seviye arayüz sağlayan bir kütüphanedir.
sns.distplot(random.uniform(size=1000), hist=False)

plt.show()
################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 4
# Question 3
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
# Algoritma karmasikligi logm + logn olarak bulundu.
#
################################################################################


import sys

def main():
    m = ["algotihm", "programminglanguages", "systemsprogramming"]
    n = ["computergraphics", "cprogramming","oop"]
    k=4
    
    print "\n"
    #print "m:", m
    #print "n:", n
    book = find_kth_book_1(m,n,k)   
    print k, "th element:", book
    #Output: oop
    print "\n\n"
    
    k=6
    #print "m:", m
    #print "n:", n 
    book = find_kth_book_1(m,n,k)
    print k, "th element:", book
    #Output: systemsprogramming
    print "\n"


################################################################################
#
# Bu metot da m, n listelerinin olup olmasigi, size'larinin verilen siradan 
# kucuk olup olmadigi kontrol edildi.
# Eger listelerin size'lari sirayi saglamiyorsa zaten oyle bir index olamayacagi
# icin eleman bulunmaz.
# Ayni sekilde m, n listeleri yoksa arama yapilmasina gerek yoktur, yine bir 
# eleman bulunamaz.
#
# Metodun karmasikligi worst case de find_kth_book_1_helper metodunun 
# karmasikligi, yani logm + logn olarak bulunur.
# Best case de ise listelerin olmamasi veya size'larinin istenilen sirayi 
# barindirmamasi durumudur. Bu durumda da Best case constant time'dir.
#
################################################################################
def find_kth_book_1(m, n, index):
    if m and n and (len(m)+len(n) >= index):
        count = 0
        index -= 1 
        #gelen input sirayi soyluyordu, index'i soylemesi icin 1 azaltildi
        
        book = find_kth_book_1_helper(m, n, index, count)
        return book
    else:
        return None

        
################################################################################
# 
# Metot da oncelikle recursive kol cagirma islemini durduran sartlar olsuturuldu.
# Bu sartlara girmeyen metot listeleri ikiye boluye, birbirleri ile karsilastiriyor
# ve karsilastirma sonucuna gore listelerin gerekli bolumleri ile recursive kol
# cagriliyor. Bu islem istenilen siraya gelinene kadar devam ediyor.
#
# Metodunun karmasikligi best case'de if sartlarindan birine girmesi durumudur,
# Bu nedenle de constant time'dir.
# Worst case ise listelein ikiye bolunerek recursive col cagrilmasi durumudur.
# Bu durumda da worst case logm + logn olarak bulunur.
#
################################################################################
def find_kth_book_1_helper(m, n, index, count):
    if not m and not n:
        return None
    elif not m:
        if len(n)<index-count:
            return None
        else:
            return n[index-count]
    elif not n:
        if len(m)<index-count:
            return None
        else:
            return m[index-count]
    else:
        if cmp(m[len(m)-1], n[0]) < 0:
            if len(m) > index-count:
                return m[index-count]
            else:
                #print "n:", n, "\tsize:", len(n), "\tindex:", index-count-1-len(m)
                count += len(m)-1
                return n[index-count-len(m)]
        elif cmp(m[0], n[len(n)-1]) > 0:
            if len(n) > index-count:
                return n[index-count-1]
            else:
                count += len(n)-1
                return m[index-count-len(n)] 
        else:
            
            m_l = []
            m_r = []
            n_l = []
            n_r = []
            
            size_m = 0
            size_n = 0
            
            if len(m) > 1:
                size_m = len(m)
                middle = (size_m+1)/2
                m_l = m[:middle]
                m_r = m[middle:]
            else:
                m_l = m
                
            if len(n) > 1:
                size_n = len(n)
                middle = (size_n+1)/2
                n_l = n[:middle]
                n_r = n[middle:]
            else:
                n_l = n
                
            
            if not m_r and not n_r:
                return find_kth_book_1_helper(m_l, n_l, index, count)
            elif not m_r:
                if cmp(n_r[0] , m_l[len(m_l)-1]) > 0:
                    return find_kth_book_1_helper(m_l, n_l, index, count)
                else:
                    if cmp(n_r[0] , m_l[0]) < 0:
                        return find_kth_book_1_helper(m_l, n_l, index, count)
                    else:
                        if cmp(n_r[len(n_r)-1], m_l[len(m_l)-1]) >= 0:
                            i = 0
                            while cmp(m_l[len(m_l)-1], n_r[i]) > 0:
                                n_l.append(n_r[i])
                                i += 1
                            
                            return find_kth_book_1_helper(m_l, n_l, index, count)
                        else:
                            n_l.extend(n_r)
                            return find_kth_book_1_helper(m_l, n_l, index, count)
            elif not n_r:
                if cmp(m_r[0] , n_l[len(n_l)-1]) > 0:
                    return find_kth_book_1_helper(n_l, m_l, index, count)
                else:
                    if cmp(m_r[0] , n_l[0]) < 0:
                            return find_kth_book_1_helper(n_l, m_l, index, count)
                    else:                        
                        if cmp(m_r[len(m_r)-1], n_l[len(n_l)-1]) > 0:
                            i = 0
                            while cmp(n_l[len(n_l)-1], m_r[i]) >= 0:
                                m_l.append(m_r[i])
                                i += 1

                            return find_kth_book_1_helper(n_l, m_l, index, count)
                        else:
                            m_l.extend(m_r)
                            return find_kth_book_1_helper(n_l, m_l, index, count)
            else:
                n_l_ok = 0
                n_r_ok = 0
                
                m_l_ok = 0
                m_r_ok = 0
            
                if cmp(n_l[len(n_l)-1], m_r[0]) < 0:
                    n_l_ok = 1
                else:
                    if cmp(n_l[len(n_l)-1], m_r[len(m_r)-1]) > 0:
                        count += len(n_l)-1 
                        m_r_ok = 1 
                    else:
                        i = 0
                        while cmp(n_l[len(n_l)-1], m_r[i]) <= 0:
                            m_l.append(m_r[i])
                            i += 1

                        m_l_ok = 1
                
                if cmp(m_l[len(n_l)-1], n_r[0]) < 0:
                    m_l_ok = 1
                else:
                    if cmp(m_l[len(m_l)-1], n_r[len(m_r)-1]) > 0:
                        count += len(m_l)-1 
                        n_r_ok = 1 
                    else:
                        i = 0
                        while cmp(m_l[len(m_l)-1], n_r[i]) <= 0:
                            n_l.append(n_r[i])
                            i += 1
                            
                        n_l_ok = 1
                                                
    
                if n_l_ok == 1 and n_r_ok == 1:
                    return find_kth_book_1_helper(n_l, n_r, index, count)    
                elif n_l_ok == 1 and m_l_ok == 1:
                    return find_kth_book_1_helper(n_l, m_l, index, count)
                elif m_l_ok == 1 and m_r_ok == 1:
                    return find_kth_book_1_helper(m_l, m_r, index, count)
                elif m_r_ok ==1 and n_r_ok == 1:
                    return find_kth_book_1_helper(m_r, n_r, index, count)
                elif m_r_ok == 1 and n_l_ok == 1:
                    return find_kth_book_1_helper(m_r, n_l, index, count)
                elif m_l_ok == 1 and n_r_ok == 1:
                    return find_kth_book_1_helper(n_l, n_r, index, count)
                else:
                    return None
    

################################################################################
#
# Denemek icin olsuturulmus bir metot.
#
################################################################################ 
def find_kth_book_1_helper_other(m, n, index, count):
    l = []
    l.extend(m)
    l.extend(n)
    l.sort()
    #print "l:", l
    return l[index-1]        
    
    
if __name__ == "__main__":
    main()       

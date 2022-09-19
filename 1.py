from hashlib import new


def filter_list(l):
        for i in li:
                
                for j in li:
                        if type(j)== str:
                                l.remove(j)
        return l    
            
            
    
#filter_list([1,2,'a','b']) == [1,2]
#
filter_list1 =[1,'a','b',0,"vb",15,"55h"] # == [1,0,15]
#filter_list1 = [1,2,'aasf','1','123',123]
sortyy=[1,'a','b',0,"vb",15,"55h"]  #11
#print(filter_list(filter_list1))
print(filter_list(sortyy))


test2 =([1, 'a', 'b', 0, 15]), [1, 0, 15]
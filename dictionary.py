customers = {"customer 1":['Firas','Male',31,'Munich','Germany','Arabic','English','German'],
             "custumer 2":['Adnan','Male',23,'Damascus','Syria','Arabic','English'],
             "customer 3":['Alaa','Male',33,'Stockholm','Sweden','Arabic','English','Swedish'],
             "customer 4":['Friend','Male',31,'Damascus','Syria','Arabic']}


def advance_invert_dict(d):
     inverse = dict()
     
     for key in d:
         
         for i in range(len(d[key])):

            val = d[key][i]
            if val not in inverse:
                inverse[val] = [key]
                
            else:
                inverse[val].append(key)
                
     print(d,"\n")
     return inverse
# call our function
print(advance_invert_dict(customers))


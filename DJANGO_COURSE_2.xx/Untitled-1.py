# c = ['vikash','kumar', 'barnwal', 'z']

# for i in range(len(c)):
#     if len(c[i]) < len(c[i+1]):
#         c[i],c[i+1] = c[i+1],c[i]

# print(c)


# a = ['vikash','kumar', 'barnwal', 'z']
# print(sorted(a, key=len))
    
c = ['vikash','kumar', 'barnwal', 'z']

new_string=""

q=len(c)
 
for i in range(q-1):
    for j in range(q-i-1):
        if c[j]>c[j+1]:
          c[j],c[j+1]=c[j+1],c[j]
      
print(c)
           







import pickle
# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple','mango','carrot']
shoplist2 = ['banana']

# Write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist, f) #dump the object to a file 
pickle.dump(shoplist2,f)
f.close()

del shoplist # detroy the shoplist variable
del shoplist2
# Read back from the storage
f = open(shoplistfile,'rb')
storedlist = pickle.load(f) # load the object from the file 
print(storedlist)
storedlist2 = pickle.load(f) # load the object from the file 
print(storedlist2)
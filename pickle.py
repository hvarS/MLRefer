import pickle

example_dict = {1:"6",2:"2",3:"f"}

#Saving the file/model
pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()


#Open The model
pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)


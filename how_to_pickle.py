# pickle
import pickle
# profile_file = open("profile.pickle", "wb") # b = binary
# profile = {"name":"Kim", "age":20, "hobby":["football", "golf", "coding"]}
# print(profile)
# pickle.dump(profile, profile_file) # save profile in the file
# profile_file.close()

profile_file = open("profile.pickle", "rb") # read, binary
profile = pickle.load(profile_file) # bring information in the file to profile
print(profile)
profile_file.close()

# a213_multi_factor.py
import multifactorcli as mfc

# create a multi-factor interface to a restricted app
my_auth = mfc.MultiFactorAuth() # This is a class object

#set the username and password
username = "banana"
password = "apple"
my_auth.set_authetication(username, password)
# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_multiFactorAuthentication(question, answer)

my_auth.run()
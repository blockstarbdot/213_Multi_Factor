# a213_multi_factor.py
import tkinter as tk
import multifactorcli as mfc

# create a multi-factor interface to a restricted app
my_auth = mfc.MultiFactorAuth()

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_multiFactorAuthentication(question, answer)

my_auth.run()
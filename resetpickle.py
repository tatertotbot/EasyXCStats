import pickle

runInfo = ["No run, this is used to initialize first run", '1/1/2001', '0', '0', '0']

with open('credentials.pickle', 'wb') as f:
    pickle.dump(runInfo, f)
    
with open('credentials.pickle', 'rb') as b:
    lastLogged = pickle.load(b)

print(lastLogged)
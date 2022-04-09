import pickle

with open("channel.pkl", "rb") as f:
    data = pickle.load(f)
    print(data)

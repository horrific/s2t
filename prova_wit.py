from wit import Wit

with open("key.txt") as f:
    access_token = f.read().split("\n")[0]

client = Wit(access_token)
resp = None

for i in range(0, 10):
    with open("audio/t" + str(i) + ".wav", 'rb') as f:
      resp = client.speech(f, None, {'Content-Type': 'audio/wav'})#mpeg3
      print(str(resp["_text"]))

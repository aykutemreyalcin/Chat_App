from client import Client
import time

# İstemcileri başlat
client1 = Client("aykut")
time.sleep(1)

client2 = Client("aaaaaaaa")
time.sleep(1)

client3 = Client("bbbbbb")
time.sleep(1)

# Mesaj gönderme
client1.send_message("Selam millet! Ben Aykut.")
time.sleep(1)

client2.send_message("Merhaba Aykut!")
time.sleep(1)

client3.send_message("Herkese selamlar.")
time.sleep(1)

# Biraz bekleyelim, sonra istemciler sohbetten ayrılsın
time.sleep(2)
client3.send_message("{quit}")
time.sleep(1)
client2.send_message("{quit}")
time.sleep(1)
client1.send_message("{quit}")

# Biraz bekleyelim, sonra program bitsin
time.sleep(1)

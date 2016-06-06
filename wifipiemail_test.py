import wifipiemail


msg = "\r\n".join([
  "From: WiFiPiRi Message Service",
  "To: Myself",
  "Subject: Note-SSID Detected",
  "",
  "Why, oh why"
  ])

wifipiemail.send_message(msg)

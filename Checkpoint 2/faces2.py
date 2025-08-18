def main():
  emoji = input("write somthingb and add an emoticon")
  convert(emoji)

def convert(message):
   message = message.replace(":)", "🙂").replace(":(","🙁")
   print(message)

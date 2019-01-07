import urllib.request
import datetime

try:
    stream = urllib.request.urlopen("https://acturis.pl")
    print(stream.read())

except urllib.request.HTTPError as err:
    print("Błąd HTTP")

except urllib.request.ContentTooShortError:
    print("Odpowiedź serwera za krótka")

except Exception as err:
    with open("error.log", 'a') as fh:
        fh.write("{0}: {1}\n".format(datetime.datetime.now(), str(err)))

finally:
    stream.close()

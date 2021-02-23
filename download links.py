import webbrowser
import requests

while True:
    try:
        chunk_size = 256
        name = input("what file name do you want:")
        names = name + ".mp4"
        url = input("Paste or write the link:")
        print("-----plz wait----")
        r = requests.get(url, stream=True)
        with open(names, "wb")as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
        print("again(1),exit(2)")
        again = input("-:-")
        if again == "2":
            break
        else:
            print("ok")
    except:
        print("Try again")

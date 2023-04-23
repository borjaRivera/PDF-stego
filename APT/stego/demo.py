from engine import Encoder, Decoder

def main():
    e = Encoder()


    img, name = e.encode("this is some text.")
    #img.show()
    print(name)

    d = Decoder()
    d.decode(name, show=True)

if __name__ == "__main__":
    main()

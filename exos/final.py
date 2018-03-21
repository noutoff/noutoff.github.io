def d(s):
    return "".join(chr(((ord(c) % ord('a') - 4) % 26)
                       + ord('a')) if c.islower() else c for c in s)

def e(s):
    return "".join(chr((1 + (ord(c) % ord('a') + 4) % 26)
                       + ord('a')) if c.islower() else c for c in s)


def obfuscated_main():

    nbazw = raw_input(d('Gyiww? ')).lower()
    dsqlm = "xufhjtiinyd"
    cnxkw = sum(map(ord, list(nbazw)))
    qjdu = cnxkw - cnxkw - 2*(cnxkw | (~cnxkw)) - 1
    while max(cnxkw, 0) and qjdu:
        if any(len(set(x+y))==2 for x,y in zip(e(nbazw) + '0'*len(dsqlm), dsqlm+'0'*len(nbazw))):
            print d('Ysyv kyiww aew avsrk. Tvc ekemr!')
            return
        else:
            print d('Csrkvexw! Ysyv kyiww mw gsvvigx.')
            return
        qjdu = (cnxkw | cnxkw) - (cnxkw & cnxkw)
    else:
        if any(len(set(x+y))==2 for x,y in zip(e(nbazw), str(cnxkw))):
            print d('Gvsyrh Csrxvsp xs Mensv Tsq')
            return
        else:
            print d("Ysy'vi rsx izir xvcmrk xs kyiww?")
            return

if __name__ == "__main__":
    obfuscated_main()

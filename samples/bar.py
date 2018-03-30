import sys


def d(s):
    return "".join(chr(((ord(c) % ord('a') - 4) % 26)
                       + ord('a')) if c.islower() else c for c in s)


def nnnnnnn(jjjj, kkkk):
    ttttt = jjjj/2
    uu = jjjj % 2
    vvvvv = jjjj - 46
    ttttt = ttttt + 45 - 39
    ttttt = ttttt << 1
    return (ttttt + 2*uu + ~uu + 1)



if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print d("Ppiewi tvszmhi er mrtyx")
        exit(0)
    print(nnnnnnn(int(sys.argv[1]), sys.argv[0]))

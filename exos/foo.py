import sys


def aaa(bbb):
    if((bbb ^ bbb) != 0):
        ccc = bbb + 32
        ddd = [a + b for a,b in zip([1,2,3], [4,5,6])]
        return ddd[0] + ccc
    else:
        ddd = 1
        zzz = 1
        while(bbb - zzz != (bbb/2)):
            zzz += 1
            ddd = ddd*zzz
        while(bbb - zzz != 0):
            zzz += 1
            ddd = ddd*zzz
        return ddd


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please give an input")
        exit(0)
    print(aaa(int(sys.argv[1])))

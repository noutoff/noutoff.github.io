def  hamming_weight(x):
    res = 0
    for i in range(8):
        if(x & (1 << i)):
            res += 1
    return res

if __name__ == "__main__":
    arg = int(raw_input("Enter a number: "))
    print(bin(arg))
    print(hamming_weight(arg))

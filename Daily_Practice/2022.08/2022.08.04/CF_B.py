
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = [i+1 for i in range(n)]
        for j in range(n):
            if j == 0:
                print(*seq)
            else:
                seq[j-1], seq[j] = seq[j], seq[j-1]
                print(*seq)
    
    return 
main()
                
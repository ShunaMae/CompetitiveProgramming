# https://output-zakki.com/run_length_encoding/
def rle(s):
    n = len(s) #文字列の長さ
    ans = [] #圧縮後のリスト
    l = 0 #始点
    while l<n:
        r = l+1
        while r<n and s[l]==s[r]: #異なる文字になるまで進む
            r += 1
        ans.append((s[l], r-l)) #文字,連続する個数
        l = r #連続しなかった文字から探索を開始
    return ans

def main():
    n = int(input())
    s = list(input())
    cells = rle(s)
    empty_cells = []
    for i in range(len(cells)):
        sign, num = cells[i]
        if sign == ".":
            empty_cells.append(num)
    
    if len(empty_cells) == 0:
        return 0
    if max(empty_cells) == 1:
        return len(empty_cells)
    if max(empty_cells) == 2:
        return sum(empty_cells)
    else:
        return 2

for _ in range(int(input())):
    print(main())



N = int(input())
S = list(map(str, input().split()))

trie_tree = {}
ans = 0

for word in S:
    # 順次アップデートしているので
    current = trie_tree 

    for letter in word:
        # もうキーとして存在していれば
        if letter in current: 
            # 値をansに追加
            ans += current[letter][0]
            current[letter][0] += 1
        # キーとして存在していなければ
        else:
            # キーを追加する
            current[letter] = [1, {}]

        # 子ノードに移動する
        current = current[letter][1]

print(ans)


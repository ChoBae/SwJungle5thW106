# 1543
text = input()
user_in = input()

count = 0
jogun = 0
for i in range(len(text)):
    if i <= jogun:
        continue
    elif text[i : i+len(user_in)-1] == user_in[0 : len(user_in)-1]:
        count += 1
        jogun += len(user_in)

print(count)
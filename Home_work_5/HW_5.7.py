# Разверните строку всеми известными вам способами

# Способ 1

s = 'agatacaca'
print(s[::-1])

# Способ 2

def reverse_string1(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)


data = reverse_string1('agatacaca')
print(data)

# Способ 3

print(''.join(reversed('agatacaca')))

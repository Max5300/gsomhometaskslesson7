s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
string = s.split()
for i in range(len(string) - 1):
    if string[i].lower().startswith('м'):
        if string[i].endswith((',', '.', ':', ';', '!', '?')):  #проверяем, что вместе со словом не удалим знак препинания
            string[i] = string[i][len(string[i])-1] #если есть знак препинания, оставляем последний символ удаляемого слова (то есть сам знак препинания)
        else:
            del string[i]
print(' '.join(string))
cidade = input('Nome da sua cidade: ').strip().capitalize()
cidade = cidade.split()
if cidade[0] == "Santo":
    print(True)
else:
    print(False)

cid = input('Nome da sua cidade: ').strip().capitalize()
print(cid[:5] == 'Santo')
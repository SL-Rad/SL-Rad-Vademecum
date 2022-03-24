import itertools

intro_img = "![](img/"
nome_diapositive = "SIRM-Toracia-HRCT_del_torace_"
nome_diapositive_2 = "_of_31.png"
outro_img = ")\n\n---\n"
n = 0

num = 35
for _ in itertools.repeat(None, num):
    n = n+1
    n_str = str(n)
    print(intro_img + nome_diapositive + n_str + nome_diapositive_2 + outro_img)

presentation = print(intro_img + nome_diapositive +
                     n_str + nome_diapositive_2 + outro_img)

title = print(nome_diapositive + ".md")

# Write the file out again
with open(title, 'w') as file:
    file.write(presentation)

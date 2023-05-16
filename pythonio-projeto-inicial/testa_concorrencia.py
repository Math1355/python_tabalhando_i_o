diretorio_do_arquivo = 'D:\TI\Python\Alura\Exercicios\Python_trabalhando_com_I_O\pythonio-projeto-inicial\dados\contatos-escrita.csv'

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

with open(diretorio_do_arquivo, encoding='utf-8', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open(diretorio_do_arquivo, encoding='utf-8', mode='a') as arquivo2:
    arquivo2.write(contato_andreza)

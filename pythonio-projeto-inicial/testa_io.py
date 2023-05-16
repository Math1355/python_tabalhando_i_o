diretorio_do_arquivo = 'D:\TI\Python\Alura\Exercicios\Python_trabalhando_com_I_O\pythonio-projeto-inicial\dados\contatos-escrita.csv'
arquivo = open(diretorio_do_arquivo, encoding='utf-8', mode='a')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', 'utf-8')
#print(texto_em_bytes)
#print(type(texto_em_bytes))

contato = bytes('15,Verônica,veronica@veronica.com.br\n', 'utf-8')
arquivo.buffer.write(contato)

arquivo.close()
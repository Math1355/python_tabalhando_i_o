import contatos_utils

try:
    #diretorio_do_arquivo = 'D:\TI\Python\Alura\Exercicios\Python_trabalhando_com_I_O\pythonio-projeto-inicial\dados\contatos.csv'
    diretorio_pickle = 'D:\TI\Python\Alura\Exercicios\Python_trabalhando_com_I_O\pythonio-projeto-inicial\dados\contatos.pickle'
    diretorio_json = 'D:\TI\Python\Alura\Exercicios\Python_trabalhando_com_I_O\pythonio-projeto-inicial\dados\contatos.json'
    #contatos = contatos_utils.csv_para_contatos(diretorio_do_arquivo)
    #contatos_utils.contatos_para_pickle(contatos, diretorio_pickle)

    #contatos = contatos_utils.pickle_para_contatos(diretorio_pickle)
    #contatos_utils.contatos_para_json(contatos, diretorio_json)

    contatos = contatos_utils.json_para_contatos(diretorio_json)

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')

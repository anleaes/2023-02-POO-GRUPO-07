from pessoaFisica import PessoaFisica

def main():
    print('\n\n**********--Inscrição de Alunos--**********\n\n')

nome = input('Digite Seu Nome:')
tipoPessoa = int(input('\nVoce é PF ou PJ? Digite 1.PF 2.PJ: '))

if tipoPessoa == 1:
    cpf = input('\nDigite Seu CPF: ')
    dt_nasc = input('\nDigite Sua Data de Nascimento: ')
else:
    cnpj = input('\nDigite seu CNPJ: ')


if tipoPessoa == 1:
    p1 = PessoaFisica(nome, cpf, dt_nasc)
    print(f"\nDados do Aluno  \n\nNome: {nome} \nCpf: {cpf} \nData Nascimento: {dt_nasc}")
else:
    print('Dados da Pessoa Jurídica')






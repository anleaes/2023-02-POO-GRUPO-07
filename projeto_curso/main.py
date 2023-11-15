from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from matricula import Matricula
from curso import Curso

pessoa1 = Pessoa('Andrew', 'Rua tal')
pessoa2 = Pessoa('Uniritter', 'Rua B')
pessoa_fisica1 = PessoaFisica(pessoa1, '000.000.000-00', '27/02/2001')
pessoa_juridica1 = PessoaJuridica(pessoa2, '000.000/000', '10/10/1966', 'google')
curso1 = Curso('ADS', '20 creditos')


matricula = Matricula('12345', '13/11/2023', curso1, pessoa_fisica1, pessoa_juridica1)








from curso import Curso
from pessoaFisica import PessoaFisica
from pessoa import Pessoa

class Matricula:
    def __init__(self, numero_matricula, data_matricula, curso, pessoaFisica, PessoaJuridica):
        self.numero_matricula = numero_matricula
        self.data_matricula = data_matricula
        self.curso = curso
        self.aluno = pessoaFisica
        self.contratante = PessoaJuridica
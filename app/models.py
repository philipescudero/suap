from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}, {self.estado}'

class Nome_Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome}'

class Turno(models.Model):
    matutino = models.BooleanField(default=False)
    vespertino = models.BooleanField(default=False)
    noturno = models.BooleanField(default=False)
    integral = models.BooleanField(default=False)

    def __str__(self):
        periodos = []
        if self.matutino:
            periodos.append("Matutino")
        if self.vespertino:
            periodos.append("Vespertino")
        if self.noturno:
            periodos.append("Noturno")
        if self.integral:
            periodos.append("Integral")

        return ', '.join(periodos)

class Disciplina(models.Model):
    disciplina = models.CharField(max_length=50)
   
    def __str__(self):
        return f'{self.disciplina}'

class Pessoas(models.Model):
    professores = models.BooleanField(default=False)
    estudantes = models.BooleanField(default=False)
    coordenacao = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    data_nasc = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)  # Chave estrangeira para a tabela de Cidade
    
    def __str__(self):
        return f'Nome: {self.nome}, Professores: {self.professores}, Estudantes: {self.estudantes}, Coordenação: {self.coordenacao}, Cidade: {self.cidade}'
    
class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)
    professor = models.BooleanField(default=False)
    estudante = models.BooleanField(default=False)
    diretor = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.nome} {self.professor} {self.estudante} {self.diretor}'
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nome} {self.site} {self.telefone}'
    
class Areas(models.Model):
    nome = models.CharField(max_length=50)
    biologia = models.BooleanField(default=False)
    computacao = models.BooleanField(default=False)
    agropecuaria = models.BooleanField(default=False)
    outros = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.biologia} {self.computacao} {self.agropecuaria}'
    
class Periodos(models.Model):
    Primeiro_periodo = models.BooleanField(default=False)
    Segundo_periodo = models.BooleanField(default=False)
    Terceiro_Periodo = models.BooleanField(default=False)
    Quarto_periodo = models.BooleanField(default=False)
    Quinto_periodo = models.BooleanField(default=False)
    Sexto_periodo = models.BooleanField(default=False)
    Setimo_periodo = models.BooleanField(default=False)
    Oitavo_periodo = models.BooleanField(default=False)
    Nono_periodo = models.BooleanField(default=False)
    Decimo_periodo = models.BooleanField(default=False)

    def __str__(self):
        return f'Primeiro Período: {self.Primeiro_periodo}, Segundo Período: {self.Segundo_periodo}, Terceiro Período: {self.Terceiro_Periodo}, Quarto Período: {self.Quarto_periodo}, Quinto Período: {self.Quinto_periodo}, Sexto Período: {self.Sexto_periodo}, Setimo Período: {self.Setimo_periodo}, Oitavo Período: {self.Oitavo_periodo}, Nono Período: {self.Nono_periodo}, Décimo Período: {self.Decimo_periodo}'
    
class Manter_cursos(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    duracao_meses = models.IntegerField()
    areas = models.ForeignKey(Areas, on_delete=models.CASCADE) 
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE) 

    def __str__(self):
        return f'Nome: {self.nome}, Carga Horária: {self.carga_horaria}, Duração (meses): {self.duracao_meses}, Área: {self.areas}, Instituição: {self.instituicao}'
    
class Matriculas(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    cursos = models.ForeignKey(Manter_cursos, on_delete=models.CASCADE)
    pessoas = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField() 

    def __str__(self):
        return f'Curso: {self.cursos.nome}, Carga Horária: {self.cursos.carga_horaria}, Duração (meses): {self.cursos.duracao_meses}, Área: {self.cursos.areas}, Instituição: {self.instituicao}'
    
class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=100)
    cursos = models.ForeignKey(Manter_cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Curso: {self.cursos.nome}, Carga Horária: {self.cursos.carga_horaria}, Duração (meses): {self.cursos.duracao_meses}, Área: {self.cursos.areas}, Disciplina: {self.disciplina}'

class Frequencia(models.Model):
    cursos = models.ForeignKey(Manter_cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    faltas = models.IntegerField()  
    
    def __str__(self):
        return f'Curso: {self.cursos.nome}, Faltas: {self.faltas}, Disciplina: {self.disciplina}'

class Turmas(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    faltas = models.IntegerField()  # Corrigido o campo faltas, pois a definição estava incorreta
    nome = models.ForeignKey(Nome_Pessoa, on_delete=models.CASCADE)  # Certifique-se de que Nome_Pessoa seja o modelo correto
    
    def __str__(self):
        return f'Disciplina: {self.disciplina}, Faltas: {self.faltas}, Turno: {self.turno}, Nome: {self.nome}'
    
class Manter_cidades(models.Model):
    nome = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.CharField(max_length=2)
    
    def __str__(self):
        return f'Nome: {self.nome}, UF: {self.uf}'

class Manter_ocorrencias(models.Model):
    descricao = models.CharField(max_length=50)
    data = models.DateField()
    curso = models.ForeignKey(Areas, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome = models.ForeignKey(Nome_Pessoa, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Descrição: {self.descricao}, Data: {self.data}, Curso: {self.curso}, Disciplina: {self.disciplina}, Nome: {self.nome}'

class Manter_disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Areas, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
            
    def __str__(self):
        return f'Nome: {self.nome}, Carga Horária: {self.carga_horaria}, Curso: {self.curso}, Período: {self.periodo}'

class Manter_avaliacao(models.Model):
    TIPOS_AVALIACAO = (
        ('prova', 'Prova'),
        ('trabalho', 'Trabalho'),
        ('projeto', 'Projeto'),
        ('lista_exercicio', 'Lista de Exercício'),
    )
    
    tipo_avaliacao = models.CharField(max_length=50, choices=TIPOS_AVALIACAO)
    valor = models.IntegerField()
    curso = models.ForeignKey(Areas, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Tipo de Avaliação: {self.tipo_avaliacao}, Valor: {self.valor}, Curso: {self.curso}, Período: {self.periodo}'
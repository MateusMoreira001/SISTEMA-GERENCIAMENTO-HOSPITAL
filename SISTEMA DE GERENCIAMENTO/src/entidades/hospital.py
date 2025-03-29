hospitais = {}

def get_hospitais():
    return hospitais

def inserir_hospital(hospital):
    nome_hospital = hospital.nome
    if nome_hospital not in hospitais.keys():
        hospitais[nome_hospital] = hospital
        return True
    else:
        print('Hospital ' + nome_hospital + ' já tem cadastro')
        return False

class Hospital:
    def __init__(self, nome, entidade_mantenedora, cidade, uf):
        self.nome = nome
        self.entidade_mantenedora = entidade_mantenedora
        self.cidade = cidade
        self.uf = uf
        self.equipamentos_hospitalar = {}

    def __str__(self):
        formato = '{} {:<30} {} {:<40} {} {:<12} {} {:<2} {}'
        hospital_formatada = formato.format('|', self.nome, '|', self.entidade_mantenedora, '|', self.cidade, '|', self.uf, '|')
        return hospital_formatada

    def inserir_equipamento_hospitalar(self, equipamento_hospitalar):
        id_equipamento_hospitalar = equipamento_hospitalar.n_série
        if id_equipamento_hospitalar not in self.equipamentos_hospitalar.keys():
            self.equipamentos_hospitalar[id_equipamento_hospitalar] = equipamento_hospitalar
        else:
            print('Equipamento ' + id_equipamento_hospitalar + ' já tem cadastro no Hospital')

def set_hospitais(hospitais1):
    global hospitais
    hospitais = hospitais1

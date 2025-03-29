from entidades.empresa_manutenção import get_empresas_manutenção
from entidades.hospital import get_hospitais
from entidades.equipamento_hospitalar import Tomográfo, EquipamentoRessonânciaMagnética


agendamentos_manutenções = []

def get_agendamentos_manutenção():
    return agendamentos_manutenções
def inserir_agendamento_manutenção(agendamento_manutenção):
    if agendamento_manutenção not in agendamentos_manutenções:
        agendamentos_manutenções.append(agendamento_manutenção)
    else:
        print('Agendamento já tem cadastro --- ' + str(agendamento_manutenção))


def criar_agendamento_manutenção(nome_hospital, nome_empresa_manutenção, data):
    hospital = get_hospitais()[nome_hospital]
    if hospital is None:
        print('Hospital ' + nome_hospital + ' não cadastrada')
        return

    empresa_manutenção = get_empresas_manutenção()[nome_empresa_manutenção]
    if empresa_manutenção is None:
        print('Empresa de Manutenção ' + nome_empresa_manutenção + ' não cadastrada')
        return
    agendamento_manutenção = AgendamentoManutenção(hospital, empresa_manutenção, data)
    inserir_agendamento_manutenção(agendamento_manutenção)


def filtrar_agendamentos_manutenções(data_máxima_agendamento_manutenção, manutenção_em_dia_equipamento_hospitalar,
                                     energia_máxima_raio_x_tomografo,tipo_imagem_ressonância_magnética,
                                     prefixo_telefone_empresa_manutenção, uf_hospital):
    agendamentos_manutenções_selecionados = []
    for agendamento_manutenção in agendamentos_manutenções:
        if data_máxima_agendamento_manutenção is not None and agendamento_manutenção.data > data_máxima_agendamento_manutenção:
            continue
        excluir_agendamento = False
        for equipamento_hospitalar in agendamento_manutenção.hospital.equipamentos_hospitalar.values():
            if manutenção_em_dia_equipamento_hospitalar is not None and equipamento_hospitalar.manutenção_em_dia != manutenção_em_dia_equipamento_hospitalar:
                excluir_agendamento = True
                break
            if isinstance(equipamento_hospitalar, Tomográfo):
                if energia_máxima_raio_x_tomografo is not None and equipamento_hospitalar.energia_raio_x > energia_máxima_raio_x_tomografo:
                    excluir_agendamento = True
                    break
            elif isinstance(equipamento_hospitalar, EquipamentoRessonânciaMagnética):
                if tipo_imagem_ressonância_magnética is not None and equipamento_hospitalar.tipo_imagem != tipo_imagem_ressonância_magnética:
                    excluir_agendamento = True
                    break
        if excluir_agendamento: continue

        if prefixo_telefone_empresa_manutenção is not None and not agendamento_manutenção.empresa_manutenção.telefone.startswith(prefixo_telefone_empresa_manutenção):
            continue
        if uf_hospital is not None and agendamento_manutenção.hospital.uf != uf_hospital:
            continue
        agendamentos_manutenções_selecionados.append(agendamento_manutenção)
    return agendamentos_manutenções_selecionados


class AgendamentoManutenção:
    def __init__(self, hospital, empresa_manutenção, data):
        self.hospital = hospital
        self.empresa_manutenção = empresa_manutenção
        self.data = data

    def __str__(self):
        formato = '{} {:<30} {} {:<24} {} {:<8} {}'
        agendamento_manutenção_formatado = formato.format('|', self.hospital.nome,
                                                          '|', self.empresa_manutenção.nome, '|', str(self.data), '|')
        return agendamento_manutenção_formatado

    def str_atributos_equipamentos_hospitalar(self):
        atributos_equipamentos_hospitalares_str = ''
        tipos_imagem_ressonancia = []
        for índice, equipamento_hospitalar in enumerate(self.hospital.equipamentos_hospitalar.values()):
            if not equipamento_hospitalar.manutenção_em_dia:
                atributos_equipamentos_hospitalares_str = 'Manutenção Necessária - '
            else:
                atributos_equipamentos_hospitalares_str = 'Não Necessaria - '

            if isinstance(equipamento_hospitalar, Tomográfo):
                atributos_equipamentos_hospitalares_str += f'{equipamento_hospitalar.energia_raio_x} mSv'
            elif isinstance(equipamento_hospitalar, EquipamentoRessonânciaMagnética):
                tipos_imagem_ressonancia.append(equipamento_hospitalar.tipo_imagem)

        if tipos_imagem_ressonancia:
            atributos_equipamentos_hospitalares_str += ' -- '.join(tipos_imagem_ressonancia)

        return atributos_equipamentos_hospitalares_str

    def str_filtro(self):
        formato = '{:<8} {} {:<35} {} {:<2} {} {:<12} {}'
        filtro_formatado = formato.format(str(self.data), '|', self.str_atributos_equipamentos_hospitalar(), '|',
                                          self.hospital.uf, '|', self.empresa_manutenção.telefone, '|')
        return self.__str__() + filtro_formatado

def set_agendamentos_manutenção(agendamentos_manutenção1):
    global agendamentos_manutenção
    agendamentos_manutenção = agendamentos_manutenção1


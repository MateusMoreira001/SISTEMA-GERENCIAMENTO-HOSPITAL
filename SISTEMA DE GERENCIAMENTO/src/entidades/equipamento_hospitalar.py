equipamentos_hospitalar = []

def get_equipamentos_hospitalar():
    return equipamentos_hospitalar

def inserir_equipamento_hospitalar(equipamento_hospitalar):
    id_equipamento_hospitalar = equipamento_hospitalar.n_série
    if id_equipamento_hospitalar not in equipamentos_hospitalar.keys():
        equipamentos_hospitalar[id_equipamento_hospitalar] = equipamentos_hospitalar
        return True
    else:
        print('Equipamento' + id_equipamento_hospitalar + 'já tem cadastro')
        return False

def selecionar_equipamentos_hospitalar(fabricante=None, data_aquisição_maxima=None, manutenção_em_dia=None):
    filtros = '\nFiltros -- '
    if fabricante:
        filtros += ' - Fabricante: ' + str(fabricante)
    if data_aquisição_maxima is not None:
        filtros += ' - Data da Aquisição: ' + str(data_aquisição_maxima)
    if manutenção_em_dia is not None:
        filtros += ' - Manutenção em Dia: ' + str(manutenção_em_dia)

    equipamentos_hospitalar_selecionados = []
    for equipamento_hospitalar in equipamentos_hospitalar:
        if fabricante is not None and equipamento_hospitalar.fabricante != fabricante:
            continue
        if data_aquisição_maxima is not None and equipamento_hospitalar.data_aquisição.__lt__(data_aquisição_maxima):
            continue
        if manutenção_em_dia is not None and equipamento_hospitalar.manutenção_em_dia != manutenção_em_dia:
            continue
        equipamentos_hospitalar_selecionados.append(equipamento_hospitalar)
    return filtros, equipamentos_hospitalar_selecionados

class EquipamentoHospitalar:
    def __init__(self, n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia):
        self.n_série = n_série
        self.marca_modelo = marca_modelo
        self.fabricante = fabricante
        self.data_aquisição = data_aquisição
        self.manutenção_em_dia = manutenção_em_dia
        self.id = n_série

    def __str__(self):
        if self.manutenção_em_dia:
            manutenção_em_dia_str = ''
        else:
            manutenção_em_dia_str = 'Manutenção Necessária'
        formato = '{} {:<6} {} {:<28} {} {:<14} {} {:<8} {} {:<21} {}'
        equipamento_hospitalar_formatado = formato.format('|', self.n_série, '|',self.marca_modelo, '|', self.fabricante, '|',
                                                          str(self.data_aquisição), '|', manutenção_em_dia_str,'|')
        return equipamento_hospitalar_formatado

class Tomográfo(EquipamentoHospitalar):
    def __init__(self, n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia, energia_raio_x):
        super().__init__(n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia)
        self.energia_raio_x = energia_raio_x

    def __str__(self):
        if self.manutenção_em_dia:
            manutenção_em_dia_str = ''
        else:
            manutenção_em_dia_str = 'Manutenção Necessária'
        formato = '{} {:<6} {} {:<28} {} {:<14} {} {:<8} {} {:<21} {} {:<5} {}'
        tomográfo_formatado = formato.format('|', self.n_série, '|', self.marca_modelo, '|',
                                                          self.fabricante, '|',
                                                          str(self.data_aquisição), '|', manutenção_em_dia_str, '|', self.energia_raio_x, '|')
        return tomográfo_formatado

class EquipamentoRessonânciaMagnética(EquipamentoHospitalar):
    def __init__(self, n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia,tipo_imagem):
        super().__init__(n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia)
        self.tipo_imagem = tipo_imagem if tipo_imagem in ('T1', 'T2', 'Flair') else ''

    def __str__(self):
        if self.manutenção_em_dia:
            manutenção_em_dia_str = ''
        else:
            manutenção_em_dia_str = 'Manutenção Necessária'
        formato = '{} {:<6} {} {:<28} {} {:<14} {} {:<8} {} {:<21} {} {:<5} {}'
        EquipamentoRessonânciaMagnética_formatado = formato.format('|', self.n_série, '|', self.marca_modelo, '|',
                                             self.fabricante, '|',
                                             str(self.data_aquisição), '|', manutenção_em_dia_str, '|',
                                             self.tipo_imagem, '|')
        return EquipamentoRessonânciaMagnética_formatado


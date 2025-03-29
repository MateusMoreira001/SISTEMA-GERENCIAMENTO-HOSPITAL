
from util.gerais import imprimir_objetos, imprimir_objetos_internos, imprimir_objetos_associação_filtros, imprimir_objeto
from util.data import Data,  converte_str_para_data

from entidades.empresa_manutenção import inserir_empresa_manutenção, EmpresaManutenção, get_empresas_manutenção
from entidades.equipamento_hospitalar import Tomográfo, EquipamentoRessonânciaMagnética
from entidades.hospital import inserir_hospital, Hospital, get_hospitais
from entidades.agendamento_manutenção import criar_agendamento_manutenção, get_agendamentos_manutenção, filtrar_agendamentos_manutenções, inserir_agendamento_manutenção


def loop_opções_execução():
    sair_loop = False
    cabeçalho_empresa_manutenção = '\nEmpresas de Manutenção : cnjp - nome - telefone - email - estado'
    cabeçalho_hospital_equipamentos_hospitalares = ('\nHospitais : nome - entidade mantenedora - cidade - uf'
                                    + '\n - Equipamentos : numero de série - marca modelo - fabricante - data aquisição - manutenção em dia - Tomografo:[energia do raio x] | Equipamento de Ressonância Magnética:[tipos de imagem]')
    cabeçalho_agendamento_manutenção = ('\nAgendamento de Manutenção : nome do hospital - nome da empresa de manutenção'
                            + ' - data do agendamento')
    while not sair_loop:
        print()
        operação = ler_str('Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: imprimir Todos / <ENTER>: Parar]', retornar=True)
        if operação == None:
            break
        elif operação in ('C', 'I'):
            opção_conteúdo = ler_str('E: Empresas de Manutenção / H: Hospitais / A: Agendamentos de Manutenção / <ENTER>: retornar]', retornar=True)
            if opção_conteúdo == None:
                pass
            elif opção_conteúdo == 'E':
                if operação == 'C':
                    loop_leitura_empresas_manutenção()
                imprimir_objetos(cabeçalho_empresa_manutenção, get_empresas_manutenção().values())
            elif opção_conteúdo in 'H':
                if operação == 'C':
                    loop_leitura_hospitais()
                imprimir_hospitais_equipamentos_hospitalares(cabeçalho_hospital_equipamentos_hospitalares)
            elif opção_conteúdo == 'A':
                if operação == 'C':
                    loop_leitura_agendamentos_manutenção()
                imprimir_objetos(cabeçalho_agendamento_manutenção, get_agendamentos_manutenção())
            elif operação == 'S':
                loop_seleção_agendamentos_manutenção()
            elif operação == 'T':
                imprimir_objetos(cabeçalho_empresa_manutenção, get_empresas_manutenção().values())
                imprimir_hospitais_equipamentos_hospitalares(cabeçalho_hospital_equipamentos_hospitalares)
                imprimir_objetos(cabeçalho_agendamento_manutenção, get_agendamentos_manutenção())

def imprimir_hospitais_equipamentos_hospitalares(cabeçalho_hospital_equipamentos_hospitalares):
    print(cabeçalho_hospital_equipamentos_hospitalares)

    for índice, hospital in enumerate(get_hospitais().values()):
        imprimir_objeto(índice=índice, objeto_str=str(hospital))
        imprimir_objetos_internos(hospital.equipamentos_hospitalar.values())

def loop_leitura_empresas_manutenção():
    sair_loop = False
    print('--- Leitura de Dados das Empresas de Manutenção ---')
    while not sair_loop:
        empresa_manutenção = ler_empresa_manutenção()
        if empresa_manutenção is not None:
            inserir_empresa_manutenção(empresa_manutenção)
        else:
            print(' - ERRO : na leitura da empresa de manutenção')
        sair_loop = ler_sair_loop('cadastro de empresa_manutenção')

def loop_leitura_hospitais():
    sair_loop = False
    print('--- Leitura de Dados dos Hospitais ---')
    while not sair_loop:
        hospital = ler_hospital()
        if hospital is not None:
            inserir_hospital(hospital)
            loop_leitura_equipamentos_hospitalares_hospital(hospital)
        else:
            print(' - ERRO : na leitura do hospital')
        sair_loop = ler_sair_loop('cadastro de hospitais')

def loop_leitura_equipamentos_hospitalares_hospital(hospital):
    sair_loop = False
    print('--- Leitura de Dados dos Equipamentos do Hospital: ' + hospital.nome + ' ---')
    while not sair_loop:
        equipamento_hospitalar = ler_equipamento_hospitalar()
        if equipamento_hospitalar is not None:
            hospital.inserir_equipamento_hospitalar(equipamento_hospitalar)
        else:
            print(' - ERRO : na leitura de equipamento hospitalar')
        sair_loop = ler_sair_loop('cadastro de equipamentos do hospital')

def loop_leitura_agendamentos_manutenção():
    sair_loop = False
    print('--- Leitura de Dados de Agendamentos de manutenção ---')
    while not sair_loop:
        agendamento_manutenção = ler_agendamento_manutenção()
        if agendamento_manutenção is not None:
            inserir_agendamento_manutenção(agendamento_manutenção)
        else:
            print(' - ERRO : na leitura de agendamento de manutenção')
        sair_loop = ler_sair_loop('cadastro de agendamento de manutenção')

def ler_sair_loop(loop):
    try:
        sair = input('-- sair do loop de ' + loop + ' [S]: ')
        if sair == 'S':
            return True
    except IOError:
        pass
    return False

def loop_seleção_agendamentos_manutenção():
    sair_loop = False
    print('--- Seleção de Agendamentos de Manutenção ---')
    while not sair_loop:
        filtros, agendamentos_manutenção_selecionados = selecionar_agendamentos_manutenções()
        if filtros is not None:
            cabeçalho = ('Agendamento Manutenção : manutenção em dia do equipamento hospitalar - uf do hospital - prefixo do telefone da empresa de manutenção - data do agendamento'
                         + '\n - Tomografo:[energia do raio x] | Equipamento de Ressonância Magnética:[tipos de imagem]')
            imprimir_objetos_associação_filtros(cabeçalho, agendamentos_manutenção_selecionados, filtros)
            sair_loop = ler_sair_loop('seleção de agendamento de manutenção')

def ler_empresa_manutenção():
    cnpj = ler_str('cnpj da empresa manutenção')
    if cnpj == None:
        return None
    nome = ler_str('nome da empresa manutenção')
    if nome == None:
        return None
    telefone = ler_str('telefone da empresa manutenção')
    if telefone == None:
        return None
    email = ler_str('email da empresa manutenção')
    if email == None:
        return None
    fora_estado = ler_bool('fora do uf da empresa manutenção')
    if fora_estado == None:
        return None
    return EmpresaManutenção(cnpj, nome, telefone, email, fora_estado)

def ler_hospital():
    nome = ler_str('nome do hospital')
    if nome == None:
        return None
    entidade_mantenedora = ler_str('entidade mantenedora do hospital')
    if entidade_mantenedora == None:
        return None
    cidade = ler_str('cidade do hospital')
    if cidade == None:
        return None
    uf = ler_str('UF do hospital')
    if uf == None:
        return None
    return Hospital(nome, entidade_mantenedora, cidade, uf)


def ler_equipamento_hospitalar():
    n_série = ler_str('número de série do equipamento')
    if n_série == None:
        return None
    marca_modelo = ler_str('marca modelo do equipamento')
    if marca_modelo == None:
        return None
    fabricante = ler_str('fabricante do equipamento')
    if fabricante == None:
        return None
    data_aquisição = ler_data('data de aquisição do equipamento')
    if data_aquisição is None:
        return None
    manutenção_em_dia = ler_bool('manutenção em dia do equipamento')
    if manutenção_em_dia == None:
        return None
    espécie_equipamento = ler_str('espécie do equipamento [Tg=Tomográfo / Rm=EquipamentoRessonânciaMagnética]')
    if espécie_equipamento == 'Tg':
        energia_raio_x = ler_int_positivo('energia raio-x do Tomográfo (mSv)')
        if energia_raio_x == None:
            return None
        return Tomográfo(n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia, energia_raio_x)
    if espécie_equipamento == 'Rm':
        tipo_imagem = ler_str('Tipo da Imagem do equipamento de ressonância magnética')
        if tipo_imagem == None:
            return None
        return EquipamentoRessonânciaMagnética(n_série,  marca_modelo, fabricante, data_aquisição, manutenção_em_dia,tipo_imagem)
    else:
        return None

def ler_agendamento_manutenção():
    nome_hospital = ler_str('nome do hospital')
    if nome_hospital == None:
        return None
    nome_empresa_manutenção = ler_str('nome da empresa de manutenção')
    if nome_empresa_manutenção == None:
        return None
    data = ler_data('data do agendamento')
    if data is None:
        return None
    return criar_agendamento_manutenção(nome_hospital, nome_empresa_manutenção, data)

def selecionar_agendamentos_manutenções():
    filtros = '\nFiltros -- '
    data_máxima_agendamento_manutenção = ler_data('Data Máxima do Agendamento de Manutenção', filtro=True)
    if data_máxima_agendamento_manutenção is not None:
        filtros += 'Data Máxima do Agendamento de Manutenção: ' + str(data_máxima_agendamento_manutenção)

    manutenção_em_dia_equipamento_hospitalar = ler_bool('Manutenção em dia do Equipamento Hospitalar', filtro=True)
    if manutenção_em_dia_equipamento_hospitalar is not None:
        filtros += ' - Manutenção em dia do Equipamento Hospitalar: ' + str(manutenção_em_dia_equipamento_hospitalar)

    energia_máxima_raio_x_tomografo = ler_int_positivo('Energia Raio X do Tomográfo', filtro=True)
    if energia_máxima_raio_x_tomografo is not None:
        filtros += (' - Energia Raio X do Tomográfo: ' + str(energia_máxima_raio_x_tomografo))

    tipo_imagem_ressonância_magnética = ler_str('Tipo da Imagem Do Equipamento de Ressonancia Magnetica', filtro=True)
    if tipo_imagem_ressonância_magnética is not None:
        filtros += (' - Tipo da Imagem Do Equipamento de Ressonancia Magnetica: ' + tipo_imagem_ressonância_magnética)

    prefixo_telefone_empresa_manutenção = ler_str('Prefixo Telefone Empresa de Manutenção', filtro=True)
    if prefixo_telefone_empresa_manutenção is not None:
        filtros += '\n - Prefixo Telefone Empresa de Manutenção: ' + str(prefixo_telefone_empresa_manutenção)

    uf_hospital = ler_str('UF do Hospital', filtro=True)
    if uf_hospital is not None:
        filtros += '\n - UF do Hospital: ' + uf_hospital
    agendamentos_manutenções_selecionados = filtrar_agendamentos_manutenções(data_máxima_agendamento_manutenção, manutenção_em_dia_equipamento_hospitalar,
                                                   energia_máxima_raio_x_tomografo,tipo_imagem_ressonância_magnética,
                                                   prefixo_telefone_empresa_manutenção, uf_hospital)

    return filtros, agendamentos_manutenções_selecionados

def ler_str(dado, filtro=False, retornar=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and (filtro or retornar):
            return None
        if len(string) > 0:
            return string
    except IOError:
        pass
    print('Erro na leitura do dado: ' + dado)
    return None

def ler_int_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro:
            return None
        int_positivo = int(string)
        if int_positivo > 0:
            return int_positivo
    except ValueError:
        pass
    print('Erro na leitura/conversão do inteiro positivo: ' + dado)
    return None

def ler_float_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro:
            return None
        float_positivo = float(input('- ' + dado + ' : '))
        if float_positivo > 0.0:
            return float_positivo
    except ValueError:
        pass
    print('Erro na leitura/conversão do flutuante positivo: ' + dado)
    return None

def ler_bool(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [S/N]: ')
        if len(string) == 0 and filtro:
            return None
        if string == 'S':
            return True
        elif string == 'N':
            return False
    except ValueError:
        pass
    print('Erro na leitura do booleano: ' + dado)
    return None

def ler_data(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [dd/mm/aaaa]: ')
        if len(string) == 0 and filtro:
            return None
        data = converte_str_para_data(string)
        if data is not None:
            return data
    except IOError:
        pass
    print('Erro na leitura da data: ' + dado)
    return None








empresas_manutenção = {}

def get_empresas_manutenção(): return empresas_manutenção

def inserir_empresa_manutenção(empresa_manutenção):
    nome_empresa_manutenção = empresa_manutenção.nome
    if nome_empresa_manutenção not in empresas_manutenção.keys():
        empresas_manutenção[nome_empresa_manutenção] = empresa_manutenção
        return True
    else:
        print('Empresa de Manutenção ' + nome_empresa_manutenção + ' já tem cadastro')
        return False

def selecionar_empresas_manutenção(prefixo_telefone=None, prefixo_nome=None, uf=None):
    filtros = '\nFiltros -- '
    if prefixo_telefone is not None:
        filtros += ' - Prefixo do Telefone: ' + str(prefixo_telefone)
    if prefixo_nome is not None:
        filtros += ' - Prefixo Nome: ' + str(prefixo_nome)
    if uf is not None:
        filtros += ' - Uf: ' + str(uf)

    empresas_manutenção_selecionadas = []
    for empresa_manutenção in empresas_manutenção:
        if prefixo_telefone is not None and not empresa_manutenção.telefone.startswith(prefixo_telefone):
            continue
        if prefixo_nome is not None and not empresa_manutenção.nome.startswith(prefixo_nome):
            continue
        if uf is not None and empresa_manutenção.uf != uf:
            continue
        empresas_manutenção_selecionadas.append(empresa_manutenção)
    return filtros, empresas_manutenção_selecionadas

class EmpresaManutenção:
    def __init__(self, cnpj, nome, telefone, email, fora_estado):
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.fora_estado = fora_estado
        self.id = cnpj

    def __str__(self):
        if self.fora_estado:
            fora_estado_str = 'Fora do Estado'
        else:
            fora_estado_str = ''
        formato = '{} {:<18} {} {:<24} {} {:<9} {} {:<35} {} {:<14} {}'
        empresa_manutenção_formatado = formato.format('|', self.cnpj, '|', self.nome, '|', self.telefone, '|', self.email, '|', fora_estado_str,'|')
        return empresa_manutenção_formatado

def set_empresas_manutenção(empresas_manutenção1):
    global empresas_manutenção
    empresas_manutenção = empresas_manutenção1
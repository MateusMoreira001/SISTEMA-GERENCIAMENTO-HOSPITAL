from util.persistência_arquivo import carregar_arquivo, salvar_arquivo
from entidades.empresa_manutenção import get_empresas_manutenção, set_empresas_manutenção
from entidades.hospital import get_hospitais, set_hospitais
from entidades.agendamento_manutenção import get_agendamentos_manutenção, set_agendamentos_manutenção
from interfaces.interface_textual import loop_opções_execução

nome_arquivo = 'agendamentos_manutenção'

def salvar_aplicação():
    agendamentos_manutenção = []
    agendamentos_manutenção.append(get_empresas_manutenção())
    agendamentos_manutenção.append(get_hospitais())
    agendamentos_manutenção.append(get_agendamentos_manutenção())
    salvar_arquivo(nome_arquivo, objetos=agendamentos_manutenção)

def recuperar_aplicação():
    agendamentos_manutenção = carregar_arquivo(nome_arquivo)
    if agendamentos_manutenção is not None:
        set_empresas_manutenção(agendamentos_manutenção[0])
        set_hospitais(agendamentos_manutenção[1])
        set_agendamentos_manutenção(agendamentos_manutenção[2])

if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()




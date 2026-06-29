# customer_registration.py
# Automação do processo de Cadastro de Cliente
# Projeto: Automação Inteligente para Negócios — Senac Tech Porto Alegre RS
# Autor: Matheus Scherer | @mtscfit
# Data: 22/06/2026

import random

# ─────────────────────────────────────────────
# BANCO DE DADOS SIMULADO — clientes já cadastrados
# ─────────────────────────────────────────────

# Simula o banco de dados interno com clientes já registrados no sistema
CUSTOMER_DATABASE = {
    "123.456.789-09": {"id": "CLI-0001", "name": "Roberto Alves", "active": True},
    "987.654.321-00": {"id": "CLI-0002", "name": "Joana Martins", "active": True},
}

# Campos obrigatórios que todo novo cliente deve preencher
REQUIRED_FIELDS = ["name", "cpf", "rg", "address"]


# ─────────────────────────────────────────────
# FUNÇÕES DE ENTRADA (INPUT)
# ─────────────────────────────────────────────

def request_documents() -> dict:
    """
    [ENTRADA] Solicita os documentos obrigatórios do cliente:
    CPF, RG e Comprovante de Endereço.
    """
    print("\n" + "=" * 50)
    print("     FORMULÁRIO DE CADASTRO DE CLIENTE")
    print("=" * 50)
    print("Preencha os dados abaixo para realizar o cadastro.\n")

    # Coleta os dados digitados pelo cliente via terminal
    name    = input("Nome completo:              ").strip()
    cpf     = input("CPF (ex: 123.456.789-09):  ").strip()
    rg      = input("RG:                         ").strip()
    address = input("Comprovante de Endereço:    ").strip()

    # Retorna os dados coletados como dicionário
    return {"name": name, "cpf": cpf, "rg": rg, "address": address}


def receive_and_digitize(customer_data: dict) -> dict:
    """
    [ENTRADA] Recebe e digitaliza (ou digita) as informações
    fornecidas pelo cliente, confirmando o recebimento no sistema.
    """
    print("\n[✔] Informações recebidas. Iniciando processamento...")
    return customer_data


# ─────────────────────────────────────────────
# FUNÇÕES DE PROCESSAMENTO (PROCESSING)
# ─────────────────────────────────────────────

def validate_data(customer_data: dict) -> bool:
    """
    [PROCESSAMENTO] Realiza a validação dos dados digitados:
    - Verifica se todos os campos obrigatórios foram preenchidos
    - Valida se o CPF possui exatamente 14 caracteres (formato 000.000.000-00)
    """
    print("\n[🔍] Validando dados do cliente...")

    # for: percorre cada campo obrigatório verificando se foi preenchido
    for field in REQUIRED_FIELDS:
        if not customer_data.get(field):
            print(f"[ERRO] Campo obrigatório não preenchido: '{field}'")
            return False

    # Valida o formato do CPF: deve ter exatamente 14 caracteres
    cpf = customer_data["cpf"]
    if len(cpf) != 14:
        print(f"[ERRO] CPF inválido: '{cpf}'. Use o formato 000.000.000-00 (14 caracteres).")
        return False

    print("[✔] Dados validados com sucesso.")
    return True


def check_duplicate(cpf: str) -> bool:
    """
    [PROCESSAMENTO] Consulta o banco de dados interno para verificar
    se o cliente já possui um cadastro ativo, evitando duplicidade.
    Retorna True se o cliente JÁ existir (duplicata encontrada).
    """
    print("\n[🔍] Verificando duplicidade no banco de dados...")

    # Verifica se o CPF já está registrado no banco de dados simulado
    if cpf in CUSTOMER_DATABASE:
        existing = CUSTOMER_DATABASE[cpf]
        print(f"[⚠️ ] Cliente já cadastrado: {existing['name']} (ID: {existing['id']})")
        return True

    print("[✔] Nenhum cadastro duplicado encontrado.")
    return False


def generate_customer_id() -> str:
    """
    [PROCESSAMENTO] Vincula o novo perfil do cliente a um número de
    identificação único (ID do Cliente) gerado automaticamente.
    """
    # Gera um ID único no formato CLI-XXXX com número aleatório de 4 dígitos
    customer_id = f"CLI-{random.randint(1000, 9999)}"
    print(f"[✔] ID de cliente gerado: {customer_id}")
    return customer_id


def save_to_database(customer_data: dict, customer_id: str) -> dict:
    """
    [PROCESSAMENTO] Salva definitivamente as informações validadas
    no banco de dados do sistema.
    """
    # Cria o registro completo do novo cliente
    new_customer = {
        "id": customer_id,
        "name": customer_data["name"],
        "cpf": customer_data["cpf"],
        "rg": customer_data["rg"],
        "address": customer_data["address"],
        "active": True,
    }

    # Insere o novo cliente no banco de dados simulado usando o CPF como chave
    CUSTOMER_DATABASE[customer_data["cpf"]] = new_customer

    print(f"[✔] Cliente '{new_customer['name']}' salvo no banco de dados.")
    return new_customer


# ─────────────────────────────────────────────
# FUNÇÃO DE SAÍDA (OUTPUT)
# ─────────────────────────────────────────────

def display_success(customer: dict) -> None:
    """
    [SAÍDA] Exibe a mensagem de 'Cadastro Concluído com Sucesso' na tela
    e emite o comprovante de cadastro do cliente.
    """
    print("\n" + "=" * 50)
    print("      ✅ CADASTRO CONCLUÍDO COM SUCESSO!")
    print("=" * 50)
    print("       COMPROVANTE DE CADASTRO")
    print("-" * 50)
    print(f"  ID do Cliente:  {customer['id']}")
    print(f"  Nome:           {customer['name']}")
    print(f"  CPF:            {customer['cpf']}")
    print(f"  RG:             {customer['rg']}")
    print(f"  Endereço:       {customer['address']}")
    print(f"  Status:         {'Ativo' if customer['active'] else 'Inativo'}")
    print("=" * 50)


# ─────────────────────────────────────────────
# FLUXO PRINCIPAL — LOOP WHILE COM ELSE
# ─────────────────────────────────────────────

def main():
    """
    Fluxo principal da automação de cadastro de cliente.
    Utiliza while para permitir novas tentativas em caso de erro,
    for para validação de campos e else para encerramento limpo do loop.
    """
    print("\n👤 SISTEMA DE CADASTRO DE CLIENTE — SENAC TECH")

    max_attempts = 3   # número máximo de tentativas permitidas
    attempt = 0

    # while: mantém o sistema ativo enquanto houver tentativas disponíveis
    while attempt < max_attempts:
        attempt += 1
        print(f"\n[Tentativa {attempt} de {max_attempts}]")

        # ETAPA 1 — Entrada: solicita documentos obrigatórios ao cliente
        customer_data = request_documents()

        # ETAPA 2 — Entrada: recebe e digitaliza as informações fornecidas
        customer_data = receive_and_digitize(customer_data)

        # ETAPA 3 — Processamento: valida os dados digitados (CPF, campos obrigatórios)
        if not validate_data(customer_data):
            # Se inválido, pergunta se deseja tentar novamente
            retry = input("\nDeseja corrigir os dados e tentar novamente? (s/n): ").strip().lower()
            if retry != "s":
                break  # encerra o while antes do limite se o usuário desistir
            continue   # volta ao início do loop para nova tentativa

        # ETAPA 4 — Processamento: verifica duplicidade no banco de dados
        if check_duplicate(customer_data["cpf"]):
            retry = input("\nDeseja cadastrar outro cliente? (s/n): ").strip().lower()
            if retry != "s":
                break
            attempt = 0  # reseta tentativas para o novo cliente
            continue

        # ETAPA 5 — Processamento: gera ID único para o novo cliente
        customer_id = generate_customer_id()

        # ETAPA 6 — Processamento: salva os dados validados no banco de dados
        new_customer = save_to_database(customer_data, customer_id)

        # ETAPA 7 — Saída: exibe confirmação e emite comprovante de cadastro
        display_success(new_customer)

        break  # cadastro concluído com sucesso — encerra o while

    else:
        # else do while: executado apenas se o loop terminar SEM um break
        # ou seja, quando o número máximo de tentativas foi esgotado
        print("\n[⚠️ ] Número máximo de tentativas atingido. Cadastro não realizado.")

    print("\n[Sistema encerrado. Obrigado!]\n")


# Ponto de entrada do script
if __name__ == "__main__":
    main()

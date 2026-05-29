import random
import time

def gerar_dados():
    dados = {
        "temperatura": random.randint(20, 100),
        "bateria": random.randint(0, 100),
        "energia_solar": random.randint(0, 100),
        "comunicacao": random.choice(["ONLINE", "OFFLINE"]),
        "consumo": random.choice(["BAIXO", "MÉDIO", "ALTO"]),
        "modulo": random.choice([
            "Propulsão",
            "Navegação",
            "Comunicação",
            "Painel Solar"
        ])
    }

    return dados

def analisar_sistema(dados):

    print("===================================")
    print("       ECOSPACE MONITOR")
    print("===================================")

    print(f"Módulo: {dados['modulo']}")
    print(f"Temperatura: {dados['temperatura']}°C")
    print(f"Bateria: {dados['bateria']}%")
    print(f"Energia Solar: {dados['energia_solar']}%")
    print(f"Comunicação: {dados['comunicacao']}")
    print(f"Consumo Energético: {dados['consumo']}")

    print("\n----------- ALERTAS -----------")

    alerta = False

    if dados["temperatura"] > 80:
        print("ALERTA: Temperatura crítica detectada!")
        alerta = True

    if dados["bateria"] < 20:
        print("ALERTA: Bateria crítica!")
        print("AÇÃO: Modo economia ativado.")
        alerta = True

    if dados["energia_solar"] < 30:
        print("ALERTA: Baixa eficiência solar.")
        alerta = True

    if dados["comunicacao"] == "OFFLINE":
        print("ERRO: Comunicação perdida.")
        alerta = True

    if dados["consumo"] == "ALTO":
        print("ATENÇÃO: Consumo elevado de energia.")
        alerta = True

    if not alerta:
        print("Sistema operando normalmente.")

    print("\n===================================")

while True:

    sistema = gerar_dados()

    analisar_sistema(sistema)

    time.sleep(5)
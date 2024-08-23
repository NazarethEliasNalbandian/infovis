import pandas as pd
import chess.pgn

# Ruta del archivo PGN
pgn_file = "/Users/nazarethnalbandian/infovis/DATOS AJEDREZ/chess_com_games.pgn"

# Lista para almacenar los datos de las partidas
data = []

# Lectura del archivo PGN
with open(pgn_file) as pgn:
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break

        # Determinar el color de NachiBrBa y el resultado de la partida
        color_nachi = "Blanco" if game.headers["White"] == "NachiBrBa" else "Negro"
        resultado = game.headers["Result"]
        if resultado == "1-0":
            resultado_nachi = "Victoria" if color_nachi == "Blanco" else "Derrota"
        elif resultado == "0-1":
            resultado_nachi = "Victoria" if color_nachi == "Negro" else "Derrota"
        else:
            resultado_nachi = "Empate"
        
        # Obtener el ELO de NachiBrBa y del oponente
        if color_nachi == "Blanco":
            elo_nachi = game.headers.get("WhiteElo")
            elo_oponente = game.headers.get("BlackElo")
        else:
            elo_nachi = game.headers.get("BlackElo")
            elo_oponente = game.headers.get("WhiteElo")

        fecha_partida = game.headers.get("Date", "Desconocida")

        # Añadir los datos a la lista
        data.append({
            "Fecha de partida": fecha_partida,
            "ELO": elo_nachi,
            "ELO_oponente": elo_oponente,
            "Color": color_nachi,
            "Resultado": resultado_nachi,
        })

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
csv_file = "/Users/nazarethnalbandian/infovis/DATOS AJEDREZ/nachi_chess_games_with_opponent_elo.csv"
df.to_csv(csv_file, index=False)

print(f"Archivo CSV guardado en: {csv_file}")
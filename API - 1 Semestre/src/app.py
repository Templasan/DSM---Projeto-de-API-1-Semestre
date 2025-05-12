from flask import Flask, render_template, request
import pymysql
from pymysql.cursors import DictCursor
from bd_functions import get_db_connection, executar_consulta
import plotly.graph_objs as go
from plotly.offline import plot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/graficos")
def graficos():
    return render_template("graficos.html")

@app.route("/artigos")
def artigos():
    return render_template("artigos.html")

@app.route("/rankings", methods=["GET", "POST"])
def rankings():
    #puxando municipios para o select
    municipios = [row["MUN"] for row in executar_consulta(
        "SELECT DISTINCT MUN FROM ranking_municipios where mun <> 'None' ORDER BY MUN"
    )]

    graficos = {
        "vl_fob": "",
        "valor_agregado": "",
        "evolucao_fob": "",
        "kg_liquido": ""
    }
    municipio = None
    #Municipio ao ser selecionado faz as consulta no banco
    if request.method == "POST":
        municipio = request.form.get("municipio")

        # 1. Top VL_FOB
        dados_fob = executar_consulta(
            "SELECT PRODUTO, VALOR FROM ranking_municipios WHERE MUN = %s AND tipo_ranking = 'TOP_VL_FOB' ORDER BY VALOR DESC LIMIT 5",
            params=(municipio,)
        )
        #Gera graficos a partir da Consulta 
        if dados_fob:
            produtos = [p if len(p) <= 22 else p[:19] + "..." for p in [item["PRODUTO"] for item in dados_fob]]  #limita tamanho da string de Produto
            valores = [item["VALOR"] for item in dados_fob]  
            fig = go.Figure([go.Bar(x=produtos, y=valores, marker_color='indianred',  
                            hovertext=["<br>".join([item["PRODUTO"][i:i+60] for i in range(0, len(item["PRODUTO"]), 60)]) 
                                        for item in dados_fob],hoverinfo="text+y")])
            fig.update_layout(title={'text':"Top 5 por VL_FOB",'x':0.5}, xaxis_title="Produto",width = 540, height=410, yaxis_title="VL_FOB", hovermode ='x')
            graficos["vl_fob"] = plot(fig, output_type='div')   

        # 2. Top Valor Agregado Médio
        dados_valor_agregado = executar_consulta(
            "SELECT PRODUTO, VALOR FROM ranking_municipios WHERE MUN = %s AND tipo_ranking = 'TOP_MEDIA_VALOR_AGREGADO' ORDER BY VALOR DESC LIMIT 5",
            params=(municipio,)
        )

        if dados_valor_agregado:
            produtos = [p if len(p) <= 22 else p[:19] + "..." for p in [item["PRODUTO"] for item in dados_valor_agregado]]
            valores = [item["VALOR"] for item in dados_valor_agregado]
            fig = go.Figure([go.Bar(x=produtos, y=valores, marker_color='royalblue',
                            hovertext=["<br>".join([item["PRODUTO"][i:i+60] for i in range(0, len(item["PRODUTO"]), 60)]) 
                                        for item in dados_fob],hoverinfo="text+y")])
            fig.update_layout(title={'text':"Top 5 por Valor Agregado Médio",'x':0.5}, xaxis_title="Produto",width = 540, height=410, yaxis_title="Valor Agregado",hovermode ='x')
            graficos["valor_agregado"] = plot(fig, output_type='div')

        # 3. Evolução Anual do VL_FOB
        evolucao = executar_consulta(
            "SELECT ANO, SUM(VALOR) AS TOTAL FROM ranking_municipios WHERE MUN = %s AND tipo_ranking = 'EVOLUCAO_ANUAL_VL_FOB' GROUP BY ANO ORDER BY ANO",
            params=(municipio,)
        )
        if evolucao:
            anos = [item["ANO"] for item in evolucao]
            totais = [item["TOTAL"] for item in evolucao]
            fig = go.Figure([go.Scatter(x=anos, y=totais, mode='lines+markers', line=dict(color='green'))])
            fig.update_layout(title={'text':"Evolução Anual do VL_FOB",'x':0.5}, xaxis_title="Ano",width = 540, height=410, yaxis_title="Soma VL_FOB",)
            graficos["evolucao_fob"] = plot(fig, output_type='div')

        # 4. Top Volume (KG_LIQUIDO)
        dados_volume = executar_consulta(
            "SELECT PRODUTO, VALOR FROM ranking_municipios WHERE MUN = %s AND tipo_ranking = 'TOP_VOLUME_KG' ORDER BY VALOR DESC LIMIT 5",
            params=(municipio,)
        )

        if dados_volume:
            produtos = [p if len(p) <= 22 else p[:19] + "..." for p in [item["PRODUTO"] for item in dados_volume]]
            valores = [item["VALOR"] for item in dados_volume]
            fig = go.Figure([go.Bar(x=produtos, y=valores, marker_color='orange',
                                    hovertext=["<br>".join([item["PRODUTO"][i:i+60] for i in range(0, len(item["PRODUTO"]), 60)]) 
                                        for item in dados_fob],hoverinfo="text+y")])
            fig.update_layout(title={'text':"Top 5 por Volume (KG Líquido)", 'x':0.5}, xaxis_title="Produto",width = 540, height=410, yaxis_title="Volume",hovermode='x')
            graficos["kg_liquido"] = plot(fig, output_type='div')

    return render_template("rankings.html", municipios=municipios, graficos=graficos,municipio=municipio)




@app.route("/pesquisa", methods=["GET", "POST"])
def pesquisa():
    dados = []
    if request.method == "POST":
        anos = request.form.getlist("anos")
        
        if anos:
            placeholders = ", ".join(["%s"] * len(anos))
           
            dados = executar_consulta(f"""
                SELECT MUN, ANO, KG_LIQUIDO FROM ranking
                WHERE ANO IN ({placeholders}) AND MUN IN ('SAO JOSE DOS CAMPOS','CAMPINAS','TAUBATE')
                ORDER BY KG_LIQUIDO DESC
                LIMIT 10
            """, params=anos)

    return render_template("pesquisa.html", dados=dados)

## Área de Igão.
pdfs = {
    1: 'pdfs/as.txt',
    2: 'pdfs/rpv.txt',
} 

@app.route('/artigos/exartigo', methods=['POST'])
def carregar_arquivo():
    id_arquivo = int(request.form['id_arquivo'])

    if id_arquivo in pdfs:
        caminho = pdfs[id_arquivo]
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = f.read().split('///')
        return render_template('exartigos.html', dados=dados)
    else:
        
        return "Arquivo não encontrado!", 404

## fechamento

if __name__ == "__main__":
    app.run(debug=True)

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
    graficos = {
        "pais_evo": "",
        "valor_agregado": "",
        "evolucao_fob": "",
        "EVO_FOB_PANDEMIA_EXP": "",
        "PROD_EVO_EXP": ""
    }
    prod_evo = executar_consulta(
        "SELECT PRODUTO, VL_FOB, ANO FROM graficos WHERE TIPO = 'PROD_EVO_VLFOB_EXP' ORDER BY ano ASC"
    )
    ### 1. grafico Evolulão produtos ------------------------
    if prod_evo:
        fig = go.Figure()
        produtos = set(item["PRODUTO"] for item in prod_evo)
        for produto in produtos:
            dados_prod = [item for item in prod_evo if item["PRODUTO"] == produto]
            anos = [item["ANO"] for item in dados_prod]
            valores = [item["VL_FOB"] for item in dados_prod]
            fig.add_trace(go.Bar(x=anos, y=valores, name="",
                                hovertext=["<br>".join([item["PRODUTO"][i:i+60] for i in range(0, len(item["PRODUTO"]), 60)]) 
                                for item in dados_prod],hoverinfo="text+y"))
                          

        fig.update_layout(
            barmode='group',
            
            title={'text': "<b>Evolução do Valor FOB dos <br>5 principais produtos</b>", 'x': 0.5,'y':0.95},
            xaxis_title="Ano", yaxis_title="<b>Valor FOB (R$)</b>",
            hovermode='x unified',
            xaxis=dict(dtick =1),
            showlegend=True,
            template='plotly_white',
            margin=dict(l=60, r=30, t=80, b=60),
            hoverlabel=dict(font_color='black', font_weight='bold', bgcolor='rgba(0,0,0,0)'))
        
        
        graficos['PROD_EVO_EXP'] = plot(fig, output_type='div', config = {'responsive':True})

    evo_pandemia = executar_consulta("SELECT VL_FOB, ANO FROM graficos WHERE TIPO = 'EVO_FOB_PANDEMIA_EXP' ORDER BY ano ASC")
    ### 2. GRAFICO EVOLUÇÃO PANDEMIA -------------------------------------------------
    if evo_pandemia:
        fig = go.Figure()

        anos = [item["ANO"] for item in evo_pandemia]
        valores = [item["VL_FOB"] for item in evo_pandemia]

        fig.add_trace(go.Scatter(
            x=anos,
            y=valores,
            mode='lines+markers',
            name="VL_FOB",
            line=dict(color='royalblue', width=3),
            marker=dict(size=6),
            hovertemplate="Ano: %{x}<br>VL_FOB: R$ %{y:,.0f}<extra></extra>",
            
        ))
        #adicionar linha pandemia
        fig.add_vline(
        x=2020,
        line_width=2,
        line_dash='dash',
        line_color='red',
        annotation_text="Início da Pandemia",
        annotation_position="top right",
        annotation_font_size=12,)

        #definir layout
        fig.update_layout(
        title="<b>Evolução do Valor FOB Total por Ano</b><br><span style='font-size:16px'>Impacto da Pandemia de COVID-19 em 2020</span>",
        xaxis_title="Ano", yaxis_title="<b>Valor FOB (R$)</b>",
        template='plotly_white',
        margin=dict(l=60, r=30, t=80, b=60),
        
        showlegend=False,
        title_x=0.5, xaxis=dict(range=[2012.5, 2023.5]),
        hovermode="x unified", )

        graficos['EVO_FOB_PANDEMIA_EXP'] = plot(fig, output_type='div', config={'responsive': True})

    pais_evo = executar_consulta(
    "SELECT ANO, VL_FOB, PAIS FROM graficos WHERE tipo = 'PAIS_EVO_FOB_EXP' ORDER BY ano asc, VL_FOB asc"
)
    #### 3. GRAFICO DE EVOLUÇÃO FOB PAIS ------------------------------------------
    if pais_evo:
        fig = go.Figure()
        paises = set(item["PAIS"] for item in pais_evo)
        
        for pais in paises:
            dados_pais = [item for item in pais_evo if item["PAIS"] == pais]
            anos = [item["ANO"] for item in dados_pais]
            valores = [item["VL_FOB"] for item in dados_pais]

            fig.add_trace(go.Scatter(
                x=anos,
                y=valores,
                mode='lines+markers',
                name="",
                hovertemplate=(
                    f"<b>{pais}</b><br>" +
                    "Ano: %{x}<br>" +
                    "VL_FOB: %{y:,.0f}<extra></extra>"
                )
            ))

        fig.update_layout(
            template='plotly_white',
            title={'text': "<b>Evolução do Valor FOB por País</b>", 'x': 0.5, 'y': 0.95},
            xaxis_title="Ano",
            yaxis_title="<b> Valor FOB (R$)</b>",
            xaxis=dict(),
            hovermode='x unified',
            showlegend=True,
            margin=dict(l=60, r=30, t=80, b=60),
            hoverlabel=dict(font_color='black', font_weight='bold', bgcolor='rgba(0,0,0,0)'),
            
        )

        graficos['PAIS_EVO_FOB_EXP'] = plot(fig, output_type='div', config={'responsive': True})


    
        evo_kg_pais = executar_consulta(
    "SELECT ANO, KG_LIQUIDO, PAIS FROM graficos WHERE tipo = 'PAIS_EVO_KG_EXP' ORDER BY ano ASC"
)
    ###4.Grafico evolução por kg ------------------------------------------
    if evo_kg_pais:
        fig = go.Figure()
        
        # Agrupar por país
        paises = set(item["PAIS"] for item in evo_kg_pais)
        for pais in paises:
            dados_pais = [item for item in evo_kg_pais if item["PAIS"] == pais]
            anos = [item["ANO"] for item in dados_pais]
            valores = [item["KG_LIQUIDO"] for item in dados_pais]
            
            fig.add_trace(go.Scatter(
                x=anos,
                y=valores,
                mode='lines+markers',
                name="",
                hovertemplate=(
                    f"<b>{pais}</b><br>"
                    "Ano: %{x}<br>"
                    "KG_LIQUIDO: %{y:,}<extra></extra>"
                )
            ))

        fig.update_layout(
            title={'text': "<b>Evolução do kg Líquido por País</b>", 'x': 0.5, 'y': 0.95},
            xaxis_title="Ano",
            yaxis_title="<b>kg Líquido</b>",
            margin=dict(l=60, r=30, t=80, b=60),
            hovermode='x unified',
            template='plotly_white',
            showlegend=True,
            
        )

        graficos['PAIS_EVO_KG'] = plot(fig, output_type='div', config={'responsive': True})


    ##5. grafico comparação kg e VL fob

        comp_vl_kg = executar_consulta(
    "SELECT VL_FOB, KG_LIQUIDO, MUN FROM graficos WHERE tipo = 'COMP_VLFOB_KGLIQ_EXP' order by VL_FOB desc;"
)

    if comp_vl_kg:
        municipios = [item["MUN"] for item in comp_vl_kg]
        vl_fob = [item["VL_FOB"] for item in comp_vl_kg]
        kg_liquido = [item["KG_LIQUIDO"] for item in comp_vl_kg]

        fig = go.Figure()

        #Barra VL_FOB
        fig.add_trace(go.Bar(
            x=municipios,
            y=vl_fob,
            name='FOB',
            marker_color='indianred',
            hovertemplate="Município: %{x}<br>VL_FOB: %{y:,.0f}<extra></extra>"
        ))

        #Barra KG_LIQUIDO
        fig.add_trace(go.Bar(
            x=municipios,
            y=kg_liquido,
            name='kg',
            marker_color='steelblue',
            hovertemplate="Município: %{x}<br>KG_LIQUIDO: %{y:,.0f}<extra></extra>"
        ))

        fig.update_layout(
            barmode='group',
            title={'text': "<b>Comparativo Valor FOB e <br> kg Líquido por Município</b>", 'x': 0.5},
            xaxis_title="Município",
            yaxis_title="Valores",
            margin=dict(l=60, r=30, t=80, b=60),
            showlegend=True,
            hovermode="x unified",
            template="plotly_white"
        )

        graficos['COMP_VL_KG'] = plot(fig, output_type='div', config={"responsive": True})



    return render_template("graficos.html", graficos=graficos)




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
            fig.update_layout(title={'text':"<b>Top 5 por Valor FOB</b>",'x':0.5}, xaxis_title="Produto", 
            template='plotly_white',margin=dict(l=60, r=30, t=80, b=60),yaxis_title="<b>Valor FOB (R$)</b>", hovermode ='x')
            graficos["vl_fob"] = plot(fig, output_type='div',  config = {'responsive':True})   

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
                                        for item in dados_valor_agregado],hoverinfo="text+y")])
            fig.update_layout(title={'text':"<b>Top 5 por Valor Agregado Médio</b>",'x':0.5}, xaxis_title="Produto", yaxis_title="<b>Valor Agregado (R$)</b>",
            template='plotly_white',margin=dict(l=60, r=30, t=80, b=60),hovermode ='x')
            graficos["valor_agregado"] = plot(fig, output_type='div',  config = {'responsive':True})

        # 3. Evolução Anual do VL_FOB
        evolucao = executar_consulta(
            "SELECT ANO, SUM(VALOR) AS TOTAL FROM ranking_municipios WHERE MUN = %s AND tipo_ranking = 'EVOLUCAO_ANUAL_VL_FOB' GROUP BY ANO ORDER BY ANO",
            params=(municipio,)
        )
        if evolucao:
            anos = [item["ANO"] for item in evolucao]
            totais = [item["TOTAL"] for item in evolucao]
            fig = go.Figure([go.Scatter(x=anos, y=totais, mode='lines+markers', line=dict(color='green'))])
            fig.update_layout(title={'text':"<b>Evolução Anual do Valor FOB</b>",'x':0.5}, xaxis_title="Ano", yaxis_title="<b> Valor FOB (R$)</b>",
            template='plotly_white',margin=dict(l=60, r=30, t=80, b=60),)

            graficos["evolucao_fob"] = plot(fig, output_type='div',  config = {'responsive':True})

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
                                        for item in dados_volume],hoverinfo="text+y")])
            fig.update_layout(title={'text':"<b>Top 5 por Volume (kg Líquido)</b>", 'x':0.5}, xaxis_title="Produto", yaxis_title="<b>kg Liquido</b>",
            template='plotly_white',margin=dict(l=60, r=30, t=80, b=60),hovermode='x')
            graficos["kg_liquido"] = plot(fig, output_type='div',  config = {'responsive':True})

    return render_template("rankings.html", municipios=municipios, graficos=graficos,municipio=municipio)


## Área de Igão.
pdfs = {
    1: 'pdfs/as.txt',
    2: 'pdfs/rpv.txt',
} 

@app.route("/artigos")
def artigos():
    return render_template("artigos.html")

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

<h1 align="center"><samp>FATEC API 1º SEMESTRE</samp></h1>

Trabalho API de DSM do 1º semestre da FATEC.

<h2 align="center"><samp>Tema do Semestre</samp></h2>
Aplicação web de consulta e análise dos dados públicos de exportação/importações dos municípios de São Paulo.


<h2 align="center"><samp>Objetivo</samp></h2>
O objetivo do nosso projeto é disponibilizar uma  ferramenta de consulta e análise, capaz de realizar pesquisas intuitivas e análises comparativas dos dados públicos de importação e exportação, assim proporcionando a democratização do acesso a informação de maneira simplificada.

### Requisitos funcionais

<details>

+ RF_1	O sistema deve permitir ao usuário realizar análises comparativas entre os municípios vizinhos e de porte semelhante.
+ RF_2	O sistema deve permitir ao usuário mapear estatisticas de fornecedores e clientes
+ RF_3	O sistema deve permitir ao usuário mapeamento dos meios de transporte do escoamento de mercadorias
+ RF_4	O sistema deve possuír um protótipo, acessível ao cliente, para validação do design e fluxo de navegação antes do desenvolvimento completo.
+ RF_5	O sistema deve fornecer ao usuário uma análise de sazonalidade sobre as exportações e importações.
+ RF_6	O sistema deve fornecer ao usuário final informações de importação/exportação detalhadas e individuais de cada munícipio.
+ RF_7	O sistema deve fornecer ao usuário informações sobre a competitividade dos produtos.
+ RF_8	O sistema deve possuir ferramentas que permitam buscar por códgo NCM e aplicar filtros personalizados.
+ RF_9	O sistema deve exibir as relações de importação/exportação, com gráficos ou relatórios que ajudem o usuário a compreender claramente o impacto na economia local.
+ RF_10	O sistema deve permitir ao usuário visualização gráfica interativa, apresentando a evolução da balança comercial dos municípios no período de 2013 a 2023.
+ RF_11	O sistema deve mostrar ao usuário como politicas tarifárias ou acordos comerciais afetaram as importações/exportações.
+ RF_12	O sistema deve mostrar ao usuário se o município se concentra em exportação/importação diversificada ou em poucos produtos.
+ RF_13	O sistema deve mostrar ao usuário os riscos associados à dependêncoa de mercados específicos ou de poucos parceiros comerciais.
+ RF_14	O sistema deve ser capaz de mostrar ao usuário como o meio de transporte utilizado afeta os custos e a eficiência logística.
+ RF_15	O sistema deve ser capaz de análisar quais países tem aumentado a importação de produtos especificos dos municípios paulistas.
+ RF_16	O sistema deve mostrar ao usuário como as empresas lidam com as variações sazonais.
+ RF_17	O sistema deve mostrar ao usuário uma projeção futura aproximada dos dados e gráficos.

</details>

### Requisitos não funcionais

<details>

+ RNF_1	O sistema deve ser responsivo, garantindo que o layout se ajuste corretamente em diferentes dispositivos, como desktop, tablet e dispositivos móveis, sem comprometer a experiência do usuário.
+ RNF_2	O sistema deve ter uma navegação intuitiva, permitindo que os usuários localizem facilmente as funcionalidades e informações desejadas, sem a necessidade de treinamento ou suporte adicional.
+ RNF_3	O sistema deve ter uma documentação extensa, objetiva e atualizada, que permita o entendimento das funcionalidades do sistema.
+ RNF_4	O sistema deve possuir dados limpos e consistêntes, sem a repetição ou incongruências.

</details>

<h1 align="center"><samp>Tecnologias utilizadas</samp></h1>

![](/readme/TecnologiaUtilizadas.png)

<table align="center">
  <tr>
    <th><b>Front-end</b></th>
    <th><b>Back-end</b></th>
    <th><b>Ferramentas</b></th>
    <th><b>Comunicação</b></th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

<h2 align="center"><samp>PRODUCT BACKLOG</samp></h2>

<details>

<table align="center">
  <tr class="row0">
    <td>Rank</td>
    <td>Prioridade</td>
    <td>User Story</td>
    <td>Requisitos</td>
    <td>Critérios de aceitação</td>
    <td>Sprint</td>
    <td>Status</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Alta</td>
    <td>Como cliente, eu quero um protótipo visual do site para que eu possa validar o design e garantir que ele atenda às minhas expectativas antes do desenvolvimento completo.</td>
    <td>RF_1, RF_4, RNF_2</td>
    <td>- O protótipo deve exibir a estrutura principal e os fluxos de navegação (RF_1) conforme acordado.
 - Deve conter elementos visuais que demonstrem a apresentação dos dados e funcionalidades principais (RF_4).
 - A interface precisa ser clara e consistente, atendendo aos padrões de usabilidade e responsividade definidos (RNF_2).
 - O cliente deve conseguir fornecer feedback direto com base no protótipo apresentado.</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Alta</td>
    <td>Como empreendedor, quero poder fazer consultas nos dados de importação/exportação para saber onde investir.</td>
    <td>RF_2, RF_8, RNF_3</td>
    <td>- O sistema deve permitir consultas sobre dados de importação/exportação de forma intuitiva (RF_2).
 - Deve ser possível identificar insights e padrões que ajudem na decisão de investimento (RF_8).
 - A pesquisa e exibição dos resultados devem ser realizadas de forma eficiente e com alta performance (RNF_3).</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Média</td>
    <td>Como entusiasta, eu quero uma ferramenta de pesquisa funcional que me permita buscar dados de importação/exportação de forma simples e eficiente.</td>
    <td>RF_2, RNF_3</td>
    <td>- A ferramenta deve permitir a realização de pesquisas com termos-chave e filtros básicos (RF_2).
 - Os resultados devem ser apresentados rapidamente e sem erros, garantindo eficiência (RNF_3).
 - A interface deve ser intuitiva para usuários não especializados.</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Alta</td>
    <td>Como analista, eu quero realizar análises comparativas entre municípios vizinhos e de porte semelhante, para avaliar como as regiões se comparam em termos econômicos.</td>
    <td>RF_1, RNF_3</td>
    <td>- O sistema deve permitir a seleção de municípios para comparação (RF_1).
 - Os resultados devem ser apresentados em gráficos ou relatórios interativos.
 - A comparação deve ser realizada com base em indicadores econômicos relevantes e de forma clara (RNF_3).</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Média</td>
    <td>Como empreendedor, eu quero analisar a diversificação dos produtos no comércio municipal, para entender as variações e os padrões no mercado.</td>
    <td>RF_16, RF_5, RNF_3</td>
    <td>- O sistema deve coletar e apresentar dados que permitam visualizar a variedade de produtos comercializados (RF_16).
 - A análise deve destacar variações e tendências de diversificação (RF_5).
 - A apresentação dos resultados deve ser clara e interativa, facilitando a compreensão dos padrões (RNF_3).</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Baixa</td>
    <td>Como investidor, eu quero identificar os mercados emergentes para tomar decisões estratégicas sobre onde focar os esforços comerciais.</td>
    <td>RF_15, RNF_3</td>
    <td>- O sistema deve identificar e destacar mercados emergentes com base em indicadores de crescimento (RF_15).
 - A visualização dos mercados emergentes deve ser intuitiva e atualizada, facilitando a análise (RNF_3).
 - O usuário deve conseguir filtrar por região ou setor, se necessário.</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Média</td>
    <td>Como entusiasta, eu quero entender o impacto das políticas econômicas e tarifárias nos mercados locais, para ajustar minhas estratégias de negócios.</td>
    <td>RF_1, RF_11, RNF_3</td>
    <td>- O sistema deve exibir informações que relacionem mudanças em políticas com variações nos indicadores econômicos (RF_11).
 - Deve haver uma apresentação clara (gráficos ou relatórios) que evidencie o impacto (RF_1).
 - A informação deve ser apresentada de forma intuitiva, facilitando a análise pelo usuário (RNF_3).</td>
    <td>Concluído</td>
  </tr>
    <tr>
    <td>8</td>
    <td>Média</td>
    <td>Como analista, eu quero mapear as cadeias produtivas para entender a estrutura do mercado e as relações entre fornecedores e clientes.</td>
    <td>RF_2, RNF_3</td>
    <td>- O sistema deve permitir a visualização de fluxos e relações entre os diversos elos da cadeia produtiva (RF_2).
 - O mapeamento deve ser apresentado por meio de diagramas ou gráficos interativos.
 - A interface deve facilitar a análise dos dados mapeados, garantindo clareza e acessibilidade (RNF_3).</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Alta</td>
    <td>Como empreendedor, eu quero que a ferramenta mostre os riscos de depender de pouca variedade de produtos quando se fala de exportação e importação, para planejar melhor as operações comerciais.</td>
    <td>RF_13, RNF_3</td>
    <td>1</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>10</td>
    <td>Alta</td>
    <td>Como entusiasta, eu quero analisar as vias de transporte usadas no comércio, para entender o escoamento de produtos.</td>
    <td>RF_14, RNF_3</td>
    <td>"- O sistema deve identificar e exibir indicadores de risco relacionados à baixa diversificação (RF_13).
 - A análise de risco deve ser apresentada de forma clara, permitindo a comparação com cenários de maior diversificação.
 - A visualização deve ser interativa e de fácil compreensão (RNF_3)."</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>11</td>
    <td>Alta</td>
    <td>Como analista, eu quero analisar a sazonalidade no comércio para identificar os padrões de demanda ao longo do ano e os ajustes na produção.</td>
    <td>RF_1, RNF_3</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>12</td>
    <td>Média</td>
    <td>Como investidor, eu quero avaliar a competitividade do mercado municipal para entender o nível de concorrência e planejar estratégias de negócio.</td>
    <td>RF_12, RF_7, RNF_3</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>13</td>
    <td>Alta</td>
    <td>Como entusiasta, quero que o site esteja integrado à ferramenta de pesquisa, para poder pesquisar sem dificuldades.</td>
    <td>RF_10, RF_9, RNF_2, RNF_1, RNF_3</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>14</td>
    <td>Média</td>
    <td>Como empreendedor, eu quero ver representações gráficas das comparações de dados para facilitar a compreensão das informações.</td>
    <td>RF_1, RF_10, RF_9, RNF_2, RNF_1</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>15</td>
    <td>Baixa</td>
    <td>Como empreendedor, eu quero ver no site projeções futuras dos dados de importação e exportação, para que eu me prepare para mudanças no mercado.</td>
    <td>RF_17, RNF_2, RNF_1, RNF_3</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>16</td>
    <td>Média</td>
    <td>Como analista, eu quero usar filtros abrangentes para refinar a pesquisa, de modo a encontrar rapidamente as informações logísticas.</td>
    <td>RF_8, RNF_2, RNF_1, RNF_3</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>17</td>
    <td>Alta</td>
    <td>Como empreendedor, eu quero interagir com um mapa responsivo, para visualizar dados logisticos dos municípios em qualquer dispositivo.</td>
    <td>RF_10, RF_9, RNF_2, RNF_1</td>
    <td>2</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>18</td>
    <td>Alta</td>
    <td>Como investidor, eu quero visualizar rankings que comparem os dados de diferentes municípios, para poder tomar decisões estando informado sobre o mercado.</td>
    <td>RF_7, RNF_2, RNF_1, RNF_3</td>
    <td>3</td>
    <td>Concluído</td>
  </tr>
  <tr>
    <td>19</td>
    <td>Média</td>
    ⁣<td>Como empreendedor, eu quero uma página explicativa sobre os riscos e significados das estatísticas vistas anteriormente, para entender melhor os dados apresentados.</td>
    <td>RF_6, RNF_2, RNF_1</td>
    <td>3</td>
    <td>Concluído</td>
  </tr>
</table>

</details>

<h2 align="center"><samp>1° SPRINT BACKLOG</samp></h2>

<details>

<table>
  <tr>
	<td>Rank</td>
	<td>Prioridade</td>
	<td>User Story</td>
	<td>Status</td>
  </tr>
  
</table>

</details>

<h3 align="center">Protótipo no Figma</h3>

<h4 align="center"><a href="">Assistir pelo Youtube</a></h4>

https:

<p></p>

https://github.com/



<h2 align="center"><samp>TIME</samp></h2>

<table align="center">
  <tr>
    <th><b>Nome</b></th>
    <th><b>Função</b></th>
    <th><b>Github</b></th>
  </tr>
  <tr>
    <td>João Victor Dos Reis Santos</td>
    <td>PO</td>
    <td><a href="https://github.com/Templasan">Github</a></td>
  </tr>
  <tr>
    <td>Lucas Inácio de Carvalho</td>
    <td>SM</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
  <tr>
    <td>Pedro Henrique Alkimim</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
  <tr>
    <td>Kaique Henrique Silva Pinto</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
  <tr>
    <td>Enrico de Chiara Germano</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
    <tr>
    <td>Gabriel de Oliveira Gonçalves</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
    <tr>
    <td>Pedro Miguel Fernandes do Nascimento</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
    <tr>
    <td>Leonardo da Silva Lopes Bezerra</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
    <tr>
    <td>Laura Félix</td>
    <td>ST</td>
    <td><a href="https://github.com/">Github</a></td>
  </tr>
</table>

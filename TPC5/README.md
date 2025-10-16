Perfil:

Tomás Gomes Neves

PG60425


<img src="./imagem_TPC3.jpg" alt="Imagem PLC" width="175">

## **Explicação do Programa:**

A minha abordagem a esta tarefa foi começar por definir uma função para conseguir fornecer a data do dia em que se está a correr o código. A função utiliza uma biblioteca chamada <i>'daytime'</i>. A seguir escrevi duas linhas que lêem e guardam o que está no meu ficheiro <i>'stock.json'</i>, de maneira a conseguir ver os produtos da máquina e consequentemente comprá-los.

A seguir a isso, tratei de criar uma função para cada possível input oferecido. Comecei pela **'Listar'**, seguido da **'MOEDA'**, depois a **'SELECIONAR'** e por fim a **'SAIR'**. A parte mais difícil foi implementar o código para devolver o troco, após todas as operações. Optei por criar contadores de todas as moedas, e subtraindo ao <i>'budget'</i> o troco, começando pelas moedas maiores. Criei também uma porção de código que avalia se as certas moedas vão ou não ser devolvidas, e se não, evita que apareçam na mensagem de troco.

Por fim, criei um loop que corre sempre, sendo possível realizar quantas operações forem desejadas, apenas terminando quando dado o input **'SAIR'** ou quando não existe nenhum input. Para terminar, e quando chamada a função **'t_SAIR'**, faz um dump no <i>'stock.json'</i>, de modo a atualizar as compras realizadas.



[Resposta da Tarefa](./TPC5.py)

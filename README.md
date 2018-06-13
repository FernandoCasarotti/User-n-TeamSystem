# User-n-TeamSystem

Este programa é um sistema que permite criar, excluir e listar tanto usuários/jogadores como países/times, permitindo, ainda, a associação entre os jogadores e os times.

Seu backend desenvolvido em Python, e seu frontend contou com HTML e JavaScript, utilizando o framework Angular. Como plataforma de hospedagem, foi utilizado o App Engine, contando com outras bibliotecas e serviços do Cloud Platform para desenvolvimento da API central e dos serviços exigidos (ex.: endpoints, vendor, database).

Seu deploy atual está na versão 1.0, que não conta com o frontend entregue; portanto, através do link abaixo, será possível realizar todas as operações, mas não contando com um frontend propriamente dito, pois a conexão das APIs feita através do JavaScript não está finalizada (os arquivos 'add.js' e 'list.js' para os times e jogadores, especificamente). Por conta disso, dentro do arquivo "app.yaml" não se encontrarão as definições 'static' exigidas pelo App Engine. O HTML das páginas foi concluído, bem como os arquivos "base.js" e "route.js", responsáveis, respectivamente, por inicializar a API desenvolvida e desenhar as rotas dos links das páginas.

Já em Python, dentro dos diretórios "apis" e "resources", são encontradas as funções desenvolvidas. Juntamente com os outros arquivos (não incluindo o diretório "static") tem-se a lógica do sistema.

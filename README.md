# Projeto Interdisciplinar IV - Sistemas de Informação ESPM

<p align="center">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

# Análise de Coleções de NFT's por Data

### 2023-01

## Integrantes

- [Rafael Guimarães e link do portifólio](https://github.com/Raf-Guim)
- [Luan Figueiredo e link do portifólio](https://github.com/LuanFig)
- [Felipe Prattes e link do portifólio](https://github.com/pratesfelipe)

## Descrição do Projeto

A raspagem de dados de coleções NFT envolve a coleta automatizada de informações sobre as diferentes coleções de NFTs disponíveis em várias plataformas. As coleções de NFTs podem ser criadas por artistas, criadores de jogos, músicos, marcas famosas e muitos outros, e podem incluir arte digital exclusiva, itens virtuais colecionáveis ​​ou qualquer outro tipo de ativo digital único.

Este projeto permite obter dados valiosos sobre as coleções de NFTs, como nome da coleção, rank diário, imagem, volume, número total de itens na coleção, preço médio dos itens, contagem de donos e muito mais. Essas informações podem ser úteis para investidores, entusiastas de criptomoedas, colecionadores e pesquisadores que desejam entender melhor o mercado de NFTs.

# Detalhes de Configuração

Para funcionar corretamente, devem ser criados os seguintes arquivos/pastas nos caminhos especificados, com o conteúdo especificado:

- O arquivo `safeData.py` deve ser criado em `/`, com o conteúdo abaixo:

```
url = [Endereco da API]
connection_string = [String de conexao com o banco de dados]
apiKey = [Chave da API]
```

- O arquivo `.env` deve ser criado em `/web`, com o conteúdo abaixo:

```
app_localIp=0.0.0.0
app_port=3000
app_root=
# Não pode terminar com barra /
app_urlSite=http://localhost:3000
app_staticFilesDir=public
app_disableStaticFiles=0
app_sqlConfig_connectionLimit=30
app_sqlConfig_waitForConnections=1
app_sqlConfig_charset=utf8mb4
app_sqlConfig_host=localhost
app_sqlConfig_port=3306
app_sqlConfig_user=[USUÁRIO DO BANCO]
app_sqlConfig_password=[SENHA DO USUÁRIO DO BANCO]
app_sqlConfig_database=[NOME DO BANCO]
```

# Licença

Este projeto é licenciado sob a [MIT License](https://github.com/tech-espm/misc-template/blob/main/LICENSE).

<p align="right">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo-si-512.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

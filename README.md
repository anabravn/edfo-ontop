# ExperDF Ontology - Ontop

1. Executar container:
```sh
docker-compose up
```

2. Gravar dados na base de dados relacional:
```sh
python -m poetry run python get_data.py
```

3. Executar Protegè com plugin Ontop.
   - Utilizar driver JDBC para Mariadb: https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector

Arquivos da ontologia estão na pasta `input` já com as configurações necessárias para o acesso ao banco de dados e mapeamento.

Script para extrair os dados: https://colab.research.google.com/drive/1PziL-rP-o8KYCZyXn41GUN_FdIv-DvIM?usp=sharing

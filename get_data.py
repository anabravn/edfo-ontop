import sqlalchemy
import logging
import time
import pandas as pd

from typing import List


db_url = 'mysql://db:password@127.0.0.1/db'
data_dir = 'csv/'
files = ['papers.csv', 'authors.csv', 'devices.csv', 'paper_device.csv', 'paper_author.csv']

def csv_to_sql(db_url: str, files: List[str]):
    engine = sqlalchemy.create_engine(db_url)

    # lê todos os arquivos na lista e insere no banco de dados
    for fname in files:
        logging.info("Lendo arquivo %s", fname)

        df = pd.read_csv(data_dir + fname)

        logging.info("Inserindo arquivo %s no banco de dados", fname)

        table_name = fname.split('.')[0]
        
        # cria a tabela se ela não existe, ou só insere os novos registros
        df.to_sql(table_name, engine, if_exists="append",
                  index=False, dtype=sqlalchemy.types.VARCHAR(512))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

    start_time = time.time()

    csv_to_sql(db_url, files) 

    duration = time.time() - start_time
    logging.info("Tempo total de execução: %d segundos", duration)

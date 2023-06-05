from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import datetime

from safeData import connection_string

engine = create_engine(connection_string)


def createCollection(data):

    with Session(engine) as session, session.begin():
        try:
            session.execute(text("INSERT INTO collection (name, image) VALUES (:name, :image)"), data)
        finally:
            return 


def obtainCollection(name):
    with Session(engine) as session:
        report = {
            'name': name
        }
        colecao = session.execute(
            text("SELECT id, name, image FROM collection WHERE name = :name"), report).first()
        return colecao


def deleteCollection(name):
    with Session(engine) as session, session.begin():
        try:
            session.execute(text("DELETE FROM collection WHERE name = :name"), {'name': name})
        finally:
            return


def listCollections():

    with Session(engine) as session:
        collections = session.execute(
            text("SELECT id, name, image FROM collection ORDER BY id"))
        for collection in collections:
            print(f'\nid: {collection.id} / name: {collection.name} / image: {collection.image}')
        print('- - - - - - - - - -')
        return collections


def existReportForToday():
    with Session(engine) as session:
        today = {
            'date': datetime.datetime.now().strftime('%Y-%m-%d')
        }
        report = session.execute(text("SELECT collection_name FROM dailyReport WHERE date = :date"), today).all()

        return report


def createDailyReport(data):

    with Session(engine) as session, session.begin():
        reports = session.execute(text("SELECT * FROM dailyReport"))
    for report in reports:
        # report[9] = data relatório já existente
        # report[2] = nome da coleção do relatório já existente
        # relatorio[1] = nome da coleção do relatório a ser criado
        if (str(report[9]) == data['date'] and report[2] == data['name']):
            print(f'Já existe um relatório {data["name"]} para hoje ({data["date"]})!')
            return

    # Lógica para criar a coleção caso seja necessário
    # relatorio[1] = nome da coleção
    validaExistencia = obtainCollection(data['name'])
    if (validaExistencia == None):
        createCollection(data)
        validaExistencia = obtainCollection(data['name'])

    # Lógica para criar o relatório

    report = {
        'ranking': data['rank'],
        'collection_name': data['name'],
        'volume': data['volume'],
        'volumeChange': data['volumeChange'],
        'tokenCount': data['tokenCount'],
        'onSaleCount': data['onSaleCount'],
        'floorSale': data['floorSale'],
        'ownerCount': data['ownerCount'],
        'date': data['date'],
        'collection_id': validaExistencia[0]
    }

    with Session(engine) as session, session.begin():
        session.execute(text(
            f"INSERT INTO dailyReport (collection_id, ranking, collection_name, volume, volumeChange, tokenCount, onSaleCount, floorSale, ownerCount, date) VALUES (:collection_id, :ranking, :collection_name, :volume, :volumeChange, :tokenCount, :onSaleCount, :floorSale, :ownerCount, :date)"), report)
    print(f'Relatório {data["name"]} criado com sucesso para o dia {data["date"]}!')


def listdailyReports():

    with Session(engine) as session:
        reports = session.execute(text(
            "SELECT * FROM dailyReport INNER JOIN collection ON dailyReport.collection_id = collection.id ORDER BY date DESC"))
        for report in reports:
            print(f'collection_id: {report[11]} / ranking: {report[1]} / name: {report[2]} / volume: {report[4]} / volumeChange: {report[5]} / tokenCount: {report[6]} / onSaleCount: {report[7]} / floorSale: {report[8]} / ownerCount: {report[9]} / date: {report[10]}')
        print('- - - - - - - - - -')
        return reports
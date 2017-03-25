import json
import argparse
from model import Appartment,db
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

def load_data_from_file(file_name):
    with open(file_name,'r',encoding='utf-8') as file:
        return json.load(file)

def insert_data_to_db(appartments_data, session_db):

    for appartment in appartments_data:
        tmp_appartment = Appartment(
            id = appartment['id'],
            settlement = appartment['settlement'],
            under_construction = appartment['under_construction'],
            description = appartment['description'],
            price = appartment['price'],
            oblast_district = appartment['oblast_district'],
            living_area = appartment['living_area'],
            has_balcony = appartment['has_balcony'],
            address = appartment['address'],
            construction_year = appartment['construction_year'],
            rooms_number = appartment['rooms_number'],
            premise_area = appartment['premise_area'],
            active = appartment.get('active', True),
        )

        session_db.add(tmp_appartment)

if __name__ == '__main__' :

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Файл с данными для загрузки")
    args = parser.parse_args()

    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    session_class = sessionmaker(engine)
    session = session_class()

    insert_data_to_db(load_data_from_file(args.file),session)

    try:
        session.commit()
        print ('OK')
    except (SQLAlchemyError) as e:
        print ("Error " , e)
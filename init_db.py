#!/usr/bin/env python
import argparse
from server.database import Base, engine
from server.database import Users
from server.database import Categorys
from server.database import SeedData
from server.database import Sub_Categorys


def run(drop=True, run_seed=False):
    if drop:
        print('Dropping all tables...')
        Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine, checkfirst=True)
    user = Users()
    category = Categorys()
    seed_data = SeedData()
    sub_category = Sub_Categorys()

    if run_seed:
        print('Seeding started for user...')
        user.init_table(seed_data.users())
        print('Seeding started for category...')
        category.init_table(seed_data.categorys())
        print('Seeding started for sub_category...')
        sub_category.init_table(seed_data.sub_categorys())


parser = argparse.ArgumentParser(description="""
Initialize/update the database with data from database\seed_data.json file.
You likely want to run this on the heroku instance via:
"heroku run -- './%(prog)s'"
""")
parser.add_argument('-D', '--drop', dest='drop', action='store_true',
                    help='drop all tables first (reinitialize)')
parser.add_argument('-RS', '--runseed', dest='runseed', action='store_true',
                    help='Seeds 100 records only')

if __name__ == '__main__':
    args = parser.parse_args()
    run(drop=args.drop, run_seed=args.runseed)

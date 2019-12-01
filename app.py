import pgpubsub
import os
import psycopg2
from datetime import datetime


dt = datetime.now().isoformat()
# connecting to postgres db
con = psycopg2.connect(user = "postgres",
                      password = "user",
                      host = "172.17.0.2",
                      port = "5432",
                      database = "postgres")


pubsub = pgpubsub.connect(user = "postgres",
                      password = "user",
                      host = "172.17.0.2",
                      port = "5432",
                      database = "postgres")


path = "/home/user/test_project"

if not os.path.exists(path):
    os.makedirs(path)

filename = 'log.txt'

try:
    while True:
        pubsub.listen('item_change')
        print(pubsub.events())
        for e in pubsub.events():
            # updating logged_at
            # cursor = con.cursor()
            # update_table_query = '''update item
            #                         set logged_at=now()
            #                         where
            #                         id=1;'''
            #
            # cursor.execute(update_table_query)
            # con.commit()
            # cursor.close()
            # con.close()
            print(e.payload.encode())
            f = open(os.path.join(path, filename), "w+")
            f.write(dt+" "+str(e.payload.encode())+'\n')
            f.close()


except KeyboardInterrupt:
    pass

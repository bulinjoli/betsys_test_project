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


path = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(path):
    os.makedirs(path)

filename = 'log.txt'

pubsub.listen('item_change')
try:
    for e in pubsub.events():

        print(e.payload.encode())
        # saving in file log.txt
        f = open(os.path.join(path, filename), "a")
        f.write(dt+" "+str(e.payload.encode())+"\n")
        f.close()

        # updating logged_at, doesnt work because of connection issues
        # cursor = con.cursor()
        # update_table_query = '''update item
        #                             set logged_at=now()
        #                             where
        #                             id=1;'''
        #
        # cursor.execute(update_table_query)
        # con.commit()
        # cursor.close()
except KeyboardInterrupt:
        print('Exit')
        pass


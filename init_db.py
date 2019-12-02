import psycopg2

# connecting to postgres db
con = psycopg2.connect(user = "postgres",
                      password = "user",
                      host = "172.17.0.2", #probably going to be different in your localhost
                      port = "5432",
                      database = "postgres")

# creating table
cursor = con.cursor()
create_table_query = '''CREATE TABLE item
          (ID INT PRIMARY KEY     NOT NULL,
          status           TEXT    NOT NULL,
          updated_at       TIMESTAMPTZ DEFAULT NULL,
          logged_at        TIMESTAMPTZ DEFAULT NULL); '''


cursor.execute(create_table_query)
con.commit()
print("Table created successfully in PostgreSQL ")

# inserting some test data
cursor = con.cursor()
insert_table_query = '''INSERT INTO item(id, status, updated_at, logged_at)
                        VALUES
                           (1, 'ready for update', now(), null); '''


cursor.execute(insert_table_query)
con.commit()
print("insert table done")

# creating function to run function when something is updated
create_function = '''CREATE FUNCTION item_change() RETURNS trigger AS $notifyfunction$
                    BEGIN
                      PERFORM pg_notify('item_change',
                        $${"table name": "$$ || TG_TABLE_NAME || $$", "json": {"id": $$ || new.id || $$ , "status": $$ || new.status || $$ , "updated_at": $$ || new.updated_at || $$}}$$);
                      RETURN new;
                    END;
                    $notifyfunction$ LANGUAGE plpgsql;'''


cursor.execute(create_function)
con.commit()
print("function for item change created")

# creating trigger to run function when something is updated
create_trigger = '''CREATE TRIGGER trigger_item_change
                    AFTER UPDATE ON item
                    FOR EACH ROW EXECUTE PROCEDURE item_change();'''


cursor.execute(create_trigger)
con.commit()
print("trigger for item change created")

cursor.close()
con.close()

# setting environment
# create application and install all dependencies
install pipenv and run pipenv shell
sudo apt-get install libpq-dev python-dev
pip install psycopg2
pip install pgpubsub

#setup postgress database
docker pull postgres
docker run --name project-db -e POSTGRES_PASSWORD=user -d postgres

# run the application
python ./init_db.py
python ./app.py

#run the database on other terminal
docker exec -it project-db psql -U postgres

# check the values with
select * from item;

# change value of item by:
update item
set status='new status'
where id=1;



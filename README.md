# betsys_test_project

install docker-compose

run docker-compose up -d

# setting environment number 2 
sudo apt-get install libpq-dev python-dev
pip install psycopg2
pip install pgpubsub

docker pull postgres
docker run --name project-db -e POSTGRES_PASSWORD=user -d postgres

docker exec -it test-project psql -U postgres



# rabbitmq-docker-compose-god-damn-simple-example
Simple example of using rabbitmq with docker compose

# Build it
```bash
docker-compose up
```
Then open new terminal and go to consumer container
```bash
docker exec -it <folder-name>_consumer_1 sh
```
And run recieve.py
```bash
python ./recieve.py
```
Then open another terminal and type
```bash
docker exec -it <folder-name>_producer_1 sh
```
And run producer.py
```bash
python ./producer.py
```
That's it!

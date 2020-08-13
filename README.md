# Redis

## Install

```bash
python3 -m virtualenv venv;
source venv/bin/activate;

```

## Redis docker
- Run
  ```bash
  docker run --rm -it --name redis --net host -p 6379:6379 redis;
  ```
- Connect into docker
  ```bash
  docker exec -it redis redis-cli;
  ```

## Redis admin
- Install redis-cli: `sudo apt-get install -y redis-tools;`
- Connect from out: `redis-cli -h "localhost" -p "6379";`
- Send command line:
  ```bash
  echo "SET b hello
  SET c world" | redis-cli -h "localhost" -p "6379";
  ```
- Used memory: `redis-cli -r 100 -i 1 info | grep used_memory_human;`

## References



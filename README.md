# ETL Pipeline Assessment

## System Requirements
- Docker
- Docker-Compose
- Cron
- Access to port 80 for prod
- Access to port 80/5000, 15672, 5672, and 8080 for dev

## How to build prod
**Web**
- `docker-compose -f docker-compose.prod.yml up -d`

**Loader**
- Add the contents of ./loader/cron to the running users cron jobs
    - crontab -e and paste is not a terrible option but there are better.

## How to build dev

### Option 1:
**Web:**
- `docker-compose -f docker-compose.dev.yml up -d adminer db rabbit`
- `cd ./web`
- `python dev.py`
The application will be availabe on port 5000

**Loader**
- Run this manually: `docker-compose -f ./loader/docker-compose.yml up`

### Option 2:
- Run `docker-compose -f docker-compose.dev.yml up -d`
The application will be availabe on port 80. This is a good option to test scaling using docker-compose

**Loader**
- Run this manually: `docker-compose -f ./loader/docker-compose.yml up`

## Endpoints
### / [POST]
Send the one of the correct JSON payloads to this endpoint.G

## Future Steps
- Pull the Queue abstraction out of loader and web as they ended up being almost the same. This way the abstraction could be used by both.
- Better modularization of the loading code would make it more extensible.
- Write unit tests as opposed to just using manual system and integration tests.
- Even harsher load testing
- Automate adding to cron
- Single command deploy (this is less of a need and more of a want).
- Refactor ExtractorService to improve extensibility.


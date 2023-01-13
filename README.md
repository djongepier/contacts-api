# contacts-api

### This project can serve as a backend for a very simple contact information store.

For anyone who may find this very basic information enough:

* lastname
* initials
* firstname
* street
* house_number
* postalcode
* residence
* phone_number

Feel free to use this code.

I have developed this Web API with the following components.

* FastAPI
* FastAPI CRUDRouter

With a PostgreSQL database in mind.

### Use these environment variables:

To authenticate with the API, make a header entry in the HTTP request named "access_code" and then fill in whatever code
you have put in: "CONTACTS_API_KEY" 

The rest of the settings are for the database. I suggest another container.
* CONTACTS_DATABASE_HOST
* CONTACTS_DATABASE_PORT
* CONTACTS_DATABASE_DB
* CONTACTS_DATABASE_USER
* CONTACTS_DATABASE_PASSWORD

### Example docker-compose

For use in Portainer of with docker-compose.

---
```
Version "3"`

services:
  server:
    image: djongepier/contacts-api
    container_name: contacts-api
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - CONTACTS_DATABASE_HOST=
      - CONTACTS_DATABASE_PORT=5432
      - CONTACTS_DATABASE_DB=
      - CONTACTS_DATABASE_USER
      - CONTACTS_DATABASE_PASSWORD
    restart: always
    networks:
      - contacts-api
    ports:
      - 80:<your port>
    depends_on:
      - db
   
  db:
    image: postgres:14
    restart: always
    environment:
      - POSTGRES_USER=contacts
      - POSTGRES_PASSWORD=contacts
      - POSTGRES_DB=contacts-api
    networks:
      - contacts-api
    volumes:
      - <your directory or volume>:/var/lib/postgresql/data
```
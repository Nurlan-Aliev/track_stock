# Track Stock

Track Stock is application for accounting for goods

* Inventory Management: Track Stock can easily track your product inventory. Track Stock remembers prices, images, and the quantity of items.

* Warehouse Management: The application allows you to manage different warehouse spaces and monitor products in each of them. This is particularly useful for companies with multiple warehouses or branches.

* Retail Store Support: Track Stock helps you monitor product availability and manage them effortlessly.

* Simple and Intuitive Interface: The application is designed with user convenience in mind.

## Install
1. Use the package manager [poetry](https://python-poetry.org/docs/) to install.

```bash
poetry install
```
2. Сreate a ".env" file in the root directory of the project.

3. Add in .env file
   * SECRET_KEY - your super secret key
   * LINK - PasswordYour website domain.
   * DATABASE_URL - link to your database
   * SECRET_TOKEN_ROLLBAR.
     * Use the [Rollbar](https://rollbar.com/) service free on your account
   * The project uses cloud storage [Selectel](https://selectel.ru/) to store images
     * ACCESS_NAME - AccountNumber_UserName
     * PASSWORD - Password
     * CONTAINER - bucket

## Usage 
### To run migrations:
```bash
make build
```

### Create Superuser:
```bash
python manage.py createsuperuser
```
* Username (leave blank to use 'user')
* Email address (press enter to skip)
* Password: Create a password
* Password (again): Repeat password

### Start
To start using the application in production run:
```bash
make start
```

To start using the application in your development environment run:
```bash
make dev
```


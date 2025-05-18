# Coffee Shop
Customer: has many Orders → has many Coffees through Orders

Coffee: has many Orders → has many Customers through Orders

Order: belongs to one Customer, one Coffee

#  Setup and Preparation
- Set up a virtual environment within this directory using `pipenv`:
    ```bash
        pipenv install
        pipenv shell
    ```
- Install any necessary packages, such as `pytest` for testing:
```bash
    pipenv install pytest
```
# ATM-API

## Introduction

This project implements a simple ATM (Automated Teller Machine) system with a server-side component only. It allows users to perform basic banking operations such as checking balance, withdrawing money, and depositing money. The data is stored in memory for simplicity.

## Functionality

The following functionalities are implemented:

*   *Get Balance:* Retrieves the current balance of a specific account.
*   *Withdraw Money:* Withdraws a specified amount of money from the user's account.
*   *Deposit Money:* Deposits a specified amount of money into the user's account.

## API Endpoints

The following REST API endpoints are available:

*   GET /accounts/{account_number}/balance: Retrieves the balance of the specified account.
*   POST /accounts/{account_number}/withdraw: Withdraws money from the specified account.
*   POST /accounts/{account_number}/deposit: Deposits money into the specified account.

## Getting Started

To run the server locally, follow these steps:

1.  Clone the repository: git clone https://github.com/Bracha-Cohen-git/ATM-API
2.  Navigate to the project directory: cd ATM-API
3.  Install the required dependencies: pip install -r requirements.txt
4.  Run the server: python atm.py

## Deployment

The server is deployed on Render and can be accessed at the following URL: https://atm-api-ip7y.onrender.com

## Usage

You can use tools like curl or Postman to interact with the API.
Postman is a popular tool for testing APIs. Here's how you can use it to interact with the ATM-API:

*1. Setting up the request:*

*   Open Postman and create a new request.
*   Select the appropriate HTTP method (GET for balance, POST for withdraw/deposit).
*   Enter the URL for the endpoint (e.g., https://atm-api-ip7y.onrender.com/accounts/101010/balance).


*2. Getting the balance:*

*   For the GET request to retrieve the balance, no additional parameters are needed.  Just send the request.
*   The response will be displayed in the lower pane, showing the account number and balance in JSON format.


*3. Withdrawing money:*

*   For the POST request to withdraw money, you need to provide the amount in the request body.
*   Select the "Body" tab and choose the "JSON" format.
*   Enter the amount in the following format: {"amount": 100} (replace 100 with the desired amount).
*   Send the request. The response will show a success message and the updated balance.


*4. Depositing money:*

*   The process for depositing money is similar to withdrawing.
*   Use the POST method and the /accounts/{account_number}/deposit endpoint.
*   Provide the amount in the JSON body as you did for withdrawing.
*   Send the request. The response will show a success message and the updated balance.


*5. Handling errors:*

Postman will also display error responses if something goes wrong (e.g., invalid account number, insufficient funds). Pay attention to the HTTP status codes and error messages in the response.





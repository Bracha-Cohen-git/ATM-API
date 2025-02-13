from flask import Flask, request, jsonify

app=Flask(__name__)

# In-memory data storage (for simplicity)
accounts = {
    "101010": {"balance": 10000}, #חשבון מספר 101010 עם 10000 ש"ח
    "202020": {"balance": 20000} #חשבון מספר 202020 עם 20000 ש"ח
}

#Retrieves the current balance of a specific account.
@app.route('/accounts/<account_number>/balance', methods=['GET'])
def get_balance(account_number):
    """
        Retrieves the balance of a specific account.

        Args:
            account_number (str): The account number.

        Returns:
            JSON: A JSON object containing the account number and balance,
                  or an error message if the account is not found.
    """
    if account_number in accounts:
        return jsonify({"account_number": account_number, "balance": accounts[account_number]["balance"]})
    return jsonify({"error": "Account not found"}), 404

#Deposits a specified amount of money into the user's account.
@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit(account_number):
    """
        Deposits money into a specific account.

        Args:
            account_number (str): The account number.

        Returns:
            JSON: A JSON object containing a success message and the updated balance,
                  or an error message if the account is not found or the amount is invalid.
    """
    if account_number not in accounts:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()
    amount = data.get("amount", 0)

    if amount <=0:
        return jsonify({"error": "Invalid amount"}), 400

    accounts[account_number]["balance"] += amount
    return jsonify({"message": "Deposit successful", "balance": accounts[account_number]["balance"]})

#Withdraws a specified amount of money from the user's account.
@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw(account_number):
    """
        Withdraws money from a specific account.

        Args:
            account_number (str): The account number.

        Returns:
            JSON: A JSON object containing a success message and the updated balance,
                  or an error message if the account is not found, the amount is invalid,
                  or there are insufficient funds.
    """
    if account_number not in accounts:
        return jsonify({"error": "Account not found"}), 400

    data = request.get_json()
    amount = data.get("amount", 0)
    if amount <=0:
        return jsonify({"error": "Invalid amount"}), 400
    if amount > accounts[account_number]["balance"]:
        return jsonify({"error": "Insufficient funds"}), 400

    accounts[account_number]["balance"] -= amount
    return jsonify({"message": "Withdraw successful", "balance": accounts[account_number]["balance"]})

#הפעלת השרת
if __name__ == '__main__':
    from os import  environ
    app.run(host='0.0.0.0', port=int(environ.get("PORT", 5000)))


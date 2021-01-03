import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import AccountValue


class AccountValueDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_account_value(self):
        """Returns all account_values."""
        with self._db.session_scope() as session:
            return session.query(AccountValue)

    def delete_account_value(self, account_value_id):
        """Deletes all records in the account value table that have account value id specified. Returns the account value id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(AccountValue.account_value_id).filter_by(account_value_id=account_value_id)
            for row in results:
                marked_to_delete.append(row[0])
            account_value = session.query(AccountValue).filter_by(account_value_id=account_value_id).delete()
            session.flush()
            return marked_to_delete

    def create_account_value(self, account_id, usd_account_amount):
        """Creates a record in the account value table with the parameters specified. Returns the account value id of the record created."""
        with self._db.session_scope() as session:
            account_value = AccountValue(account_id=account_id, usd_account_amount=usd_account_amount)
            session.add(account_value)
            session.flush()
            return account_value.account_value_id

if __name__ == "__main__":
    account_value = AccountValueDAO()

    # Insert account_value functionality
    account_id = 2
    usd_account_amount = 503.162997


    id = account_value.create_account_value(account_id, usd_account_amount)
    print(id)
    # Get account_value functionality
    results = account_value.get_account_value()
    for row in results:
        print(row)

    # Delete account_value funcitonality
    print(account_value.delete_account_value(id))
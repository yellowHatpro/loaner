from celery import shared_task
from item.models import User, Transaction


@shared_task()
def calculate_user_credit_score(user):
    try:
        user = User.objects.get(email=user)
    except User.DoesNotExist:
        return "User not found"

    # Get user's transactions
    credit_transactions = Transaction.objects.filter(
        user=user, transaction_type='CREDIT')
    debit_transactions = Transaction.objects.filter(
        user=user, transaction_type='DEBIT')

    total_credit = sum(c_t.amount for c_t in credit_transactions)
    total_debit = sum(d_t.amount for d_t in debit_transactions)
    balance = total_credit - total_debit
    return f"Processed transactions for user {user}. Balance: {balance}"

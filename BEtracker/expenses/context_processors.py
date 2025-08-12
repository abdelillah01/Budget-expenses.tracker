from .models import Budget
from django.db.models import Sum
from expenses.models import Expense
from datetime import date

def user_budget(request):
    if not request.user.is_authenticated:
        return {}
    # Get budget object for current user
    try:
        budget = Budget.objects.get(user=request.user)
        budget_amount = budget.amount
        # Calculate spent this month
        today = date.today()
        spent = Expense.objects.filter(
            user=request.user, date__year=today.year, date__month=today.month
        ).aggregate(Sum("amount"))["amount__sum"] or 0
        remaining = budget_amount - spent
    except Budget.DoesNotExist:
        budget_amount = None
        spent = None
        remaining = None
    return {
        "navbar_budget": budget_amount,
        "navbar_budget_spent": spent,
        "navbar_budget_remaining": remaining,
    }

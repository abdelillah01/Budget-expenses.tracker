from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models


from datetime import date, timedelta
from django.utils import timezone
from django.shortcuts import render
from expenses.models import Expense

def home(request):
    expenses = []
    budget_amount = spent_this_month = remaining_budget = None
    current_filter = request.GET.get('filter', 'day')
    
    if request.user.is_authenticated:
        today = timezone.localdate()
        queryset = Expense.objects.filter(user=request.user)
        if current_filter == 'day':
            expenses = queryset.filter(date=today)
        elif current_filter == 'week':
            start_week = today - timedelta(days=today.weekday())
            end_week = start_week + timedelta(days=6)
            expenses = queryset.filter(date__range=[start_week, end_week])
        elif current_filter == 'month':
            expenses = queryset.filter(date__year=today.year, date__month=today.month)
        else:
            expenses = queryset.none()
        # Budget quick summary
        try:
            budget = Budget.objects.get(user=request.user)
            budget_amount = budget.amount
        except Budget.DoesNotExist:
            budget_amount = None
        spent_this_month = queryset.filter(date__year=today.year, date__month=today.month).aggregate(
            total=Sum("amount"))["total"] or 0
        remaining_budget = budget_amount - spent_this_month if budget_amount is not None else None

    context = {
        'expenses': expenses,
        'current_filter': current_filter,
        'budget_amount': budget_amount,
        'spent_this_month': spent_this_month,
        'remaining_budget': remaining_budget,
    }
    return render(request, 'home.html', context)


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})


@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
# Create your views here.


from .models import Category
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def category_list(request):
    categories = Category.objects.filter(models.Q(user=request.user) | models.Q(user__isnull=True))
    return render(request, 'expenses/category_list.html', {'categories': categories})

@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'expenses/category_form.html', {'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "expenses/category_confirm_delete.html", {"category": category})

# Analytics view to summarize expenses
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Expense, Category

@login_required
def analytics(request):
    # Monthly totals
    monthly_data = (
        Expense.objects.filter(user=request.user)
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    # Category totals
    category_data = (
        Expense.objects.filter(user=request.user)
        .values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    # Format data for Chart.js
    months = [str(d['month'])[:7] for d in monthly_data]  # 'YYYY-MM'
    month_totals = [float(d['total']) for d in monthly_data]

    categories = [d['category__name'] for d in category_data]
    category_totals = [float(d['total']) for d in category_data]

    return render(request, "expenses/analytics.html", {
        "months": months,
        "month_totals": month_totals,
        "categories": categories,
        "category_totals": category_totals,
    })


from .models import Budget, Expense
from .forms import BudgetForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum

@login_required
def manage_budget(request):
    budget, created = Budget.objects.get_or_create(
        user=request.user, defaults={'amount': 0}
    )
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('manage_budget')
    else:
        form = BudgetForm(instance=budget)
    # Calculate spent amount this month
    
    
    from datetime import date
    from django.db.models.functions import TruncMonth
    today = date.today()
    month_spent = Expense.objects.filter(
        user=request.user, 
        date__year=today.year, date__month=today.month
    ).aggregate(Sum("amount"))['amount__sum'] or 0
    remaining = budget.amount - month_spent

    return render(request, "expenses/budget.html", {
        "form": form,
        "budget": budget.amount,
        "spent": month_spent,
        "remaining": remaining,
    })
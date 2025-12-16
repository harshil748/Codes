from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .forms import CustomUserCreationForm, BookForm, BorrowerForm
from .models import Book, Borrower


def is_admin(user):
    return user.is_staff


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()
    return render(request, "library/signup.html", {"form": form})


@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect("admin_dashboard")
    else:
        return redirect("client_dashboard")


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    books = Book.objects.all()
    borrowers = Borrower.objects.all()
    return render(
        request,
        "library/admin_dashboard.html",
        {"books": books, "borrowers": borrowers},
    )


@login_required
def client_dashboard(request):
    available_books = Book.objects.filter(is_available=True)
    try:
        borrower = Borrower.objects.get(user=request.user, return_date__isnull=True)
        borrowed_book = borrower.borrowed_book
    except Borrower.DoesNotExist:
        borrowed_book = None

    return render(
        request,
        "library/client_dashboard.html",
        {"available_books": available_books, "borrowed_book": borrowed_book},
    )


@login_required
@user_passes_test(is_admin)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = BookForm()
    return render(
        request, "library/book_form.html", {"form": form, "title": "Add Book"}
    )


@login_required
@user_passes_test(is_admin)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = BookForm(instance=book)
    return render(
        request, "library/book_form.html", {"form": form, "title": "Edit Book"}
    )


@login_required
@user_passes_test(is_admin)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("admin_dashboard")
    return render(request, "library/delete_confirm.html", {"object": book})


@login_required
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    # Check if book is available
    if not book.is_available:
        return redirect("client_dashboard")

    # Check if user already has a borrowed book
    existing_borrow = Borrower.objects.filter(
        user=request.user, return_date__isnull=True
    ).first()
    if existing_borrow:
        return redirect("client_dashboard")

    # Create borrower record
    borrower = Borrower(
        user=request.user,
        name=request.user.username,
        email=request.user.email,
        borrowed_book=book,
    )
    borrower.save()

    # Update book availability
    book.is_available = False
    book.save()

    return redirect("client_dashboard")


@login_required
def return_book(request):
    try:
        borrower = Borrower.objects.get(user=request.user, return_date__isnull=True)
        book = borrower.borrowed_book

        # Update borrower record
        borrower.return_date = timezone.now()
        borrower.save()

        # Update book availability
        book.is_available = True
        book.save()

    except Borrower.DoesNotExist:
        pass

    return redirect("client_dashboard")

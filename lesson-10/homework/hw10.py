 Homework 1: ToDo List Application
python
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False  # False = incomplete, True = complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        return f"{self.title} | Due: {self.due_date} | {'Done' if self.status else 'Pending'}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete(self):
        for task in self.tasks:
            if not task.status:
                print(task)


# CLI
def main():
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. Mark Complete\n3. List All\n4. List Incomplete\n5. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date: ")
            todo.add_task(Task(title, desc, due))
        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            for t in todo.tasks:
                if t.title == title:
                    t.mark_complete()
        elif choice == "3":
            todo.list_tasks()
        elif choice == "4":
            todo.list_incomplete()
        elif choice == "5":
            break

# Uncomment to run
# main()
 Homework 2: Simple Blog System
python
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content

    def latest_posts(self, n=3):
        for post in self.posts[-n:]:
            print(post)


# CLI
def blog_cli():
    blog = Blog()
    while True:
        print("\n1. Add Post\n2. List All\n3. Posts by Author\n4. Delete Post\n5. Edit Post\n6. Latest Posts\n7. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author = input("Author: ")
            blog.posts_by_author(author)
        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Title to edit: ")
            new_content = input("New content: ")
            blog.edit_post(title, new_content)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break

# Uncomment to run
# blog_cli()
 Homework 3: Simple Banking System
python
class Account:
    def __init__(self, acc_number, holder, balance=0):
        self.acc_number = acc_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account {self.acc_number} | Holder: {self.holder} | Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account

    def check_balance(self, acc_number):
        acc = self.accounts.get(acc_number)
        if acc: print(acc.balance)

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
            else:
                print("Overdraft not allowed!")

    def account_details(self, acc_number):
        acc = self.accounts.get(acc_number)
        if acc: print(acc)


# CLI
def bank_cli():
    bank = Bank()
    while True:
        print("\n1. Add Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Account Details\n7. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            acc_num = input("Account number: ")
            holder = input("Holder name: ")
            bank.add_account(Account(acc_num, holder))
        elif choice == "2":
            acc_num = input("Account number: ")
            bank.check_balance(acc_num)
        elif choice == "3":
            acc_num = input("Account number: ")
            amt = int(input("Amount: "))
            bank.accounts[acc_num].deposit(amt)
        elif choice == "4":
            acc_num = input("Account number: ")
            amt = int(input("Amount: "))
            bank.accounts[acc_num].withdraw(amt)
        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amt = int(input("Amount: "))
            bank.transfer(from_acc, to_acc, amt)
        elif choice == "6":
            acc_num = input("Account number: ")
            bank.account_details(acc_num)
        elif choice == "7":
            break

# Uncomment to run
# bank_cli()

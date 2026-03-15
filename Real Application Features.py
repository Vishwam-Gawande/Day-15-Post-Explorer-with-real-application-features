import requests
import json

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch posts
response = requests.get(url)
posts = response.json()

saved_posts = []


def load_saved_posts():
    global saved_posts
    try:
        with open("saved_posts.json", "r") as file:
            saved_posts = json.load(file)
    except:
        saved_posts = []


def save_to_file():
    with open("saved_posts.json", "w") as file:
        json.dump(saved_posts, file)
    print("Saved posts stored.")


def show_first_posts():
    for post in posts[:10]:
        print(post["id"], "-", post["title"])


def search_posts():
    keyword = input("Enter keyword: ").lower()

    for post in posts:
        if keyword in post["title"].lower():
            print(post["id"], "-", post["title"])


def read_post():
    try:
        post_id = int(input("Enter post ID: "))
    except:
        print("Please enter a valid number.")
        return

    for post in posts:
        if post["id"] == post_id:
            print("\nTitle:", post["title"])
            print("Body:", post["body"])
            return

    print("Post not found.")


def save_post():
    try:
        post_id = int(input("Enter post ID to save: "))
    except:
        print("Please enter a valid number.")
        return

    # prevent duplicates
    for post in saved_posts:
        if post["id"] == post_id:
            print("Post already saved.")
            return

    for post in posts:
        if post["id"] == post_id:
            saved_posts.append(post)
            print("Post saved!")
            return

    print("Post not found.")


def view_saved_posts():
    if not saved_posts:
        print("No saved posts.")
        return

    for post in saved_posts:
        print(post["id"], "-", post["title"])


def delete_saved_post():
    try:
        post_id = int(input("Enter saved post ID to delete: "))
    except:
        print("Please enter a valid number.")
        return

    for post in saved_posts:
        if post["id"] == post_id:
            saved_posts.remove(post)
            print("Post deleted successfully.")
            return

    print("Saved post not found.")


def show_menu():
    print("\n====== POST EXPLORER ======")
    print("1 Show first 10 posts")
    print("2 Search posts")
    print("3 Read post by ID")
    print("4 Save post")
    print("5 View saved posts")
    print("6 Delete saved post")
    print("7 Exit")


load_saved_posts()

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        show_first_posts()

    elif choice == "2":
        search_posts()

    elif choice == "3":
        read_post()

    elif choice == "4":
        save_post()

    elif choice == "5":
        view_saved_posts()

    elif choice == "6":
        delete_saved_post()

    elif choice == "7":
        save_to_file()
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
from flask import Flask
import random

app = Flask(__name__)

# print(__name__)

r1 = random.randint(1, 9)

@app.route("/")  # python decorator
def title_header():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")


@app.route("/<int:num>")
def guess(num):
    if num == r1:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/fl4MZmeXzPfrYh4FeR/giphy.gif'/>")
    elif num > r1:
        return ("<h1 style='color:blue'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/MGbi9O1ByAzv32qr00/giphy.gif'/>")
    else:
        return ("<h1 style='color:red'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/3oEhmUTjJpmB7WcIMg/giphy-downsized-large.gif'/>")


# @app.route("/user/<name>/<int:post_id>")
# def show_id(post_id, name):
#     return f"Post, {post_id}"

#
# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"
#     return wrapper

#
# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"
#     return wrapper
#
#
# def make_underline(function):
#     def wrapper():
#         return f"<u>{function()}</u>"
#     return wrapper
#
#
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underline
# def bye():
#     return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
categories = [
    [1, "Ages 3–6"],
    [2, "Ages 6–9"],
    [3, "Ages 9–12"],
    [4, "Ages 12–15"],
]

books = [
     #Picture Book Adventures (Ages 3–6)
 [1, 1, "Becoming Real--The True Story of The Velveteen Rabbit", "Molly Golden", "978-0358681540", 13.6, "book2.jpg", 0],
 [2, 1, "The Lorax", "Dr. Seuss", "978-0394823379", 16.99, "book3.jpg", 1],
 [3, 1, "The Won't Quit Kid", " David Pollack & Brave Books", '978-1955550826', 18.99, "book6.jpg", 0],
 [4, 1, "The Ugly Duckling", "H.C. Andersen & Lisa McCue ", "978-0307121066", 11.41, "book7.jpg", 1],

    # Growing Readers (Ages 6–9)
  [5, 2, "Charlotte's Web", "E. B. White", "978-0062658753", 5.69, "book4.jpg", 1],
  [6, 2, "Matilda", " Roald Dahl & Quentin Blake", "978-0670824397", 10.24, "book8.jpg", 1],
  [7, 2, "Diary of a Wimpy Kid, Book 1", "Jeff Kinney", "978-0810993136", 12.51, "book9.jpg", 0],
  [8, 2, "Dinosaurs Before Dark (Magic Tree House, No. 1)", "Mary Pope Osborne & Sal Murdocca", " 978-0679824114", 3.69, "book10.jpg", 0],

    # Young Explorers (Ages 9–12)
  [9, 3, "Harry Potter and the Goblet of Fire", "J. K. Rowling", "978-1338878950", 5.95, "book1.jpg", 1],
  [10, 3, "The Lightning Thief (Percy Jackson and the Olympians, Book 1)", "Rick Riordan", "978-0786838653", 5.50, "book11.jpg", 0],
  [11, 3, "On the Edge of the Dark Sea of Darkness: The Wingfeather Saga Book 1", " Andrew Peterson & Joe Sutphin", "978-0307446657", 9.99, "book12.jpg", 0],
  [12, 3, "The Adventures of Robin Hood", "Roger Lancelyn Green", "978-0141329383", 5.84, "book13.jpg", 1],

    # Teen Dreamers (Ages 12–15)
  [13, 4, "One of Us Is Lying", "Karen M. McManus", "978-1524714680", 15.99, "book5.jpg", 0],
  [14, 4, "Six of Crows", "Leigh Bardugo", "978-1627792127", 11.99, "book14.jpg", 1],
  [15, 4, "The Outsiders", "S. E. Hinton", "978-0670532575", 10.99, "book15.jpg", 0],
  [16, 4, "The Book Thief", "Markus Zusak", "978-0375842207", 7.79, "book16.jpg", 1],
]

@app.route('/')
def home():
    return render_template("index.html", categories=categories)

@app.route('/category')
def category():
    category_id = request.args.get("categoryId", type=int)
    selected_books = [b for b in books if b[1] == category_id]
    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search', '')
    return render_template('index.html', query=query, categories=categories)
    
@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html', error=e) 

if __name__ == "__main__":
    app.run(debug = True)

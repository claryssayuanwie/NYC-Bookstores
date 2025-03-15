from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

# Fully complete dataset with all required fields
bookstores = [
    {
        "id": 1,
        "title": "The Strand Bookstore",
        "image": "https://static01.nyt.com/images/2019/01/31/arts/31strand2-promo/31strand2-promo-superJumbo-v2.jpg",
        "summary": "Largest indie bookstore in NYC! Open since 1927. Family-owned. Shop online at strandbooks.com",
        "location": "828 Broadway, New York, NY 10003",
        "price_range": "$$",
        "rating": 4.8,
        "year_established": 1927,
        "popular_books": ["To Kill a Mockingbird", "1984", "The Great Gatsby"],
        "events": ["Author Readings", "Book Signings", "Poetry Nights"],
        "similar_bookstores": [2, 3, 5]
    },
    {
        "id": 2,
        "title": "The Drama Book Shop",
        "image": "https://dramabookshop.com/cdn/shop/files/DBS1-060621DD-scaled.jpg?v=1672345282&width=3840",
        "summary": "The Drama Book Shop is a legendary bookstore dedicated to plays, screenplays, and theater literature. Founded in 1917, it has been a cornerstone of New York’s theater community for over a century. It was saved from closure by Lin-Manuel Miranda and his team, who transformed it into a stunning literary space. The store frequently hosts playwriting workshops, Broadway book clubs, and theater-related discussions.",
        "location": "266 W 39th St, New York, NY 10018",
        "price_range": "$$",
        "rating": 4.7,
        "year_established": 1917,
        "popular_books": ["Hamilton: The Revolution", "Shakespeare's Complete Works", "Rent: The Complete Book"],
        "events": ["Playwriting Workshops", "Broadway Book Clubs", "Theater Talk Panels"],
        "similar_bookstores": [1, 4, 6]
    },
    {
        "id": 3,
        "title": "McNally Jackson Books",
        "image": "https://images.ctfassets.net/1aemqu6a6t65/13is8PwclIzUs0R9mHaNBv/266dc6bf0a9cd2c56de5e4ab2ef6cec8/Mc-Nally-Jackson-Seaport-Manhattan-NYC-Photo-Mike-Szpot-on-behalf-of-the-Seaport.jpg",
        "summary": "McNally Jackson Books is a beloved independent bookstore known for its carefully curated selection of fiction, non-fiction, and poetry. It also features a cozy café, making it an ideal spot for reading, writing, or working. The bookstore actively supports local authors and frequently hosts book launches and literary discussions. Its inviting atmosphere attracts students, writers, and intellectuals from all over the city.",
        "location": "52 Prince St, New York, NY 10012",
        "price_range": "$$",
        "rating": 4.6,
        "year_established": 2004,
        "popular_books": ["Normal People", "Where the Crawdads Sing", "The Midnight Library"],
        "events": ["Book Signings", "Author Q&A Sessions", "Literary Discussions"],
        "similar_bookstores": [1, 5, 7]
    },
    {
        "id": 4,
        "title": "Books Are Magic",
        "image": "https://cdn.shopify.com/s/files/1/0080/8372/files/Tattly_SmallBusiness_BooksAreMagic_13_HIRES_2048x2048.jpg?v=1583937611",
        "summary": "Books Are Magic is a charming bookstore founded by bestselling author Emma Straub. Located in Brooklyn, it has quickly become a favorite for its warm, community-focused approach to bookselling. The store is known for its excellent children’s book section, welcoming environment, and stunning storefront mural. It regularly hosts family-friendly events, author talks, and writing workshops.",
        "location": "225 Smith St, Brooklyn, NY 11231",
        "price_range": "$$",
        "rating": 4.9,
        "year_established": 2017,
        "popular_books": ["A Man Called Ove", "Circe", "The House in the Cerulean Sea"],
        "events": ["Storytime for Kids", "Meet the Author", "Writing Workshops"],
        "similar_bookstores": [2, 6, 8]
    },
    {
        "id": 5,
        "title": "Albertine Books",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e9/One_kid_exploring_the_Albertine_Books_in_the_Cultural_Services_of_the_French_Embassy.jpg",
        "summary": "Albertine Books is a hidden gem inside the French Embassy, specializing in French and English literature. The store’s celestial ceiling and tranquil ambiance make it a peaceful retreat for book lovers. It has an extensive selection of philosophy, poetry, and world literature. The bookstore frequently hosts French literature-themed events and bilingual readings.",
        "location": "972 5th Ave, New York, NY 10075",
        "price_range": "$$",
        "rating": 4.5,
        "year_established": 2014,
        "popular_books": ["Madame Bovary", "Les Misérables", "The Little Prince"],
        "events": ["French Book Readings", "Literary Salons", "Translation Workshops"],
        "similar_bookstores": [1, 3, 9]
    },
    {
        "id": 6,
        "title": "Bluestockings Cooperative",
        "image": "https://images.ctfassets.net/1aemqu6a6t65/7ckVQWrpKZRLJfLpbdOEEC/363bdfe1e541a37dede390e0db563b2c/floor_angle",
        "summary": "A feminist and activist bookstore serving as a radical community space for social justice and LGBTQ+ topics. It operates as a worker-owned cooperative, promoting diverse voices and ethical goods. The store sells books on feminism, race, and queer studies, while also hosting activism events. Bluestockings is more than a bookstore—it’s a hub for change and dialogue.",
        "location": "116 Suffolk St, New York, NY 10002",
        "price_range": "$",
        "rating": 4.6,
        "year_established": 1999,
        "popular_books": ["Sister Outsider", "Feminism is for Everybody", "Queer Theory"],
        "events": ["Activist Meetups", "Queer Book Club", "Social Justice Panels"],
        "similar_bookstores": [2, 4, 10]
    },
    {
        "id": 7,
        "title": "Rizzoli Bookstore",
        "image": "https://images.food52.com/DVVahU_Ew7vKgjmmPnAiBKEGZ-k=/b10cd49f-d19c-464c-90b6-3f4e37798850--20040245356_5778b31b3f_b.jpg",
        "summary": "Rizzoli Bookstore is an elegant and historic bookstore specializing in art, design, photography, and fashion books. Originally opened in 1964, it has been a destination for artists, designers, and book lovers for decades. The store is known for its beautifully designed interior, offering a luxurious reading experience. Rizzoli also hosts art book signings, photography lectures, and design talks.",
        "location": "1133 Broadway, New York, NY 10010",
        "price_range": "$$$",
        "rating": 4.8,
        "year_established": 1964,
        "popular_books": ["The Art of War", "Chanel: Collections and Creations", "Van Gogh: The Life"],
        "events": ["Art Book Signings", "Photography Lectures", "Design Talks"],
        "similar_bookstores": [3, 4, 8]
    },
    {
        "id": 8,
        "title": "Housing Works Bookstore",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/23/HousingWorksCafe-April2015.jpg",
        "summary": "Housing Works Bookstore is a nonprofit bookstore and café dedicated to fighting homelessness and the AIDS crisis. It operates entirely on donated books and volunteers, ensuring that all proceeds go toward its mission. The store has a warm and inviting atmosphere, making it a great place to browse books, have coffee, and support a meaningful cause. It frequently hosts poetry readings, book launches, and community gatherings to engage New Yorkers in social activism.",
        "location": "126 Crosby St, New York, NY 10012",
        "price_range": "$",
        "rating": 4.7,
        "year_established": 1998,
        "popular_books": ["The Glass Castle", "The Catcher in the Rye", "The Sun Also Rises"],
        "events": ["Poetry Readings", "Community Gatherings", "Book Sales"],
        "similar_bookstores": [4, 6, 9]
    },
    {
        "id": 9,
        "title": "Argosy Book Store",
        "image": "https://argosybooks.cdn.bibliopolis.com/images/upload//carousel_26_1.jpg?auto=webp&v=1492636595",
        "summary": "Argosy Book Store is New York City's oldest independent bookstore, specializing in rare and antique books. Established in 1925, it has a world-class collection of first editions, signed books, and historical documents. The store is a treasure trove for collectors and history buffs, offering a glimpse into literary and cultural history. Argosy also holds rare book auctions and appraisal days, making it a must-visit for bibliophiles.",
        "location": "116 E 59th St, New York, NY 10022",
        "price_range": "$$$",
        "rating": 4.9,
        "year_established": 1925,
        "popular_books": ["First Edition Classics", "Rare Manuscripts", "Signed Biographies"],
        "events": ["Rare Book Auctions", "Collector Meetups", "Appraisal Days"],
        "similar_bookstores": [5, 8, 10]
    },
    {
        "id": 10,
        "title": "Three Lives & Company",
        "image": "https://media.villagepreservation.org/wp-content/uploads/2020/05/15062806/IMG_7525-1024x683.jpg",
        "summary": "Three Lives & Company is a small but beloved West Village bookstore known for its highly personalized book recommendations. It has a cozy, intimate atmosphere that encourages deep literary exploration and conversation. The staff takes pride in curating a thoughtful selection of books, ensuring every visitor leaves with something special. The store frequently hosts reading groups and literary discussions, fostering a tight-knit community of book lovers.",
        "location": "154 W 10th St, New York, NY 10014",
        "price_range": "$$",
        "rating": 4.8,
        "year_established": 1978,
        "popular_books": ["The Night Circus", "The Secret History", "A Little Life"],
        "events": ["Book Recommendation Nights", "Literary Discussions", "Reading Groups"],
        "similar_bookstores": [6, 7, 9]
    }
]


@app.route("/")
def index():
    featured = random.sample(bookstores, 3)  # Select 3 random bookstores
    return render_template("homepage.html", bookstores=featured)

@app.route("/featured")
def featured():
    return jsonify(random.sample(bookstores, 3))

@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    results = [
        b for b in bookstores if
        query in b["title"].lower() or
        query in b["location"].lower() or
        query in b["summary"].lower()
    ]
    return render_template("search.html", query=query, results=results)

@app.route("/api/featured")
def featured_bookstores():
    featured = random.sample(bookstores, 3)  # Select 3 random bookstores
    return jsonify(featured)


@app.route("/view/<int:bookstore_id>")
def view_bookstore(bookstore_id):
    bookstore = next((b for b in bookstores if b["id"] == bookstore_id), None)
    if not bookstore:
        return "<h1>Bookstore Not Found</h1>", 404
    return render_template("view.html", bookstore=bookstore, bookstores=bookstores)

def suggest_similar_bookstores(new_store):
    similarity_scores = []
    
    for b in bookstores:
        if b["id"] == new_store["id"]:
            continue  # Skip itself
        score = 0
        if new_store["price_range"] == b["price_range"]:
            score += 1
        if new_store["location"].split(",")[-1] == b["location"].split(",")[-1]:  # Match by city
            score += 1
        if any(book in b["popular_books"] for book in new_store["popular_books"]):
            score += 2
        if any(event in b["events"] for event in new_store["events"]):
            score += 2
        
        similarity_scores.append((b["id"], score))

    # Sort by highest similarity and return the top 3
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    return [b_id for b_id, _ in similarity_scores[:3]]  # Return top 3 bookstore IDs


@app.route("/add", methods=["GET", "POST"])
def add_bookstore():
    if request.method == "POST":
        new_id = max(b["id"] for b in bookstores) + 1 if bookstores else 1
        new_store = {
            "id": new_id,
            "title": request.form["title"],
            "image": request.form["image"],
            "summary": request.form["summary"],
            "location": request.form["location"],
            "price_range": request.form["price_range"],
            "rating": float(request.form["rating"]),
            "year_established": int(request.form["year_established"]),
            "popular_books": [book.strip() for book in request.form["popular_books"].split(",")],
            "events": [event.strip() for event in request.form["events"].split(",")],
            "similar_bookstores": []
        }

        # Auto-suggest similar bookstores
        new_store["similar_bookstores"] = suggest_similar_bookstores(new_store)

        bookstores.append(new_store)

        # 🔥 Redirect directly to the new bookstore's page
        return redirect(url_for("view_bookstore", bookstore_id=new_id))

    return render_template("add.html", bookstores=bookstores)



@app.route("/edit/<int:bookstore_id>", methods=["GET", "POST"])
def edit_bookstore(bookstore_id):
    bookstore = next((b for b in bookstores if b["id"] == bookstore_id), None)
    if not bookstore:
        return "<h1>Bookstore Not Found</h1>", 404

    if request.method == "POST":
        try:
            # Get form data (added summary!)
            title = request.form.get("title")
            image = request.form.get("image")
            summary = request.form.get("summary")  # <-- Add this line
            location = request.form.get("location")
            price_range = request.form.get("price_range")
            rating = request.form.get("rating")
            year_established = request.form.get("year_established")
            popular_books = request.form.get("popular_books").split(",")
            events = request.form.get("events").split(",")

            if not title:
                return "<h1>Error: Title is missing</h1>", 400  

            # Update bookstore
            bookstore["title"] = title
            bookstore["image"] = image
            bookstore["summary"] = summary  # <-- Add this line
            bookstore["location"] = location
            bookstore["price_range"] = price_range
            bookstore["rating"] = float(rating)
            bookstore["year_established"] = int(year_established)
            bookstore["popular_books"] = [b.strip() for b in popular_books]
            bookstore["events"] = [e.strip() for e in events]

            return redirect(url_for("view_bookstore", bookstore_id=bookstore_id))

        except Exception as e:
            return f"<h1>Error updating bookstore</h1><p>{e}</p>", 400  

    return render_template("edit.html", bookstore=bookstore, bookstores=bookstores, edit=True)


@app.route("/add_api", methods=["POST"])
def add_api():
    new_id = max(b["id"] for b in bookstores) + 1 if bookstores else 1
    new_store = {
        "id": new_id,
        "title": request.form["title"],
        "image": request.form["image"],
        "summary": request.form["summary"],
        "location": request.form["location"],
        "price_range": request.form["price_range"],
        "rating": float(request.form["rating"]),
        "year_established": int(request.form["year_established"]),
        "popular_books": [book.strip() for book in request.form["popular_books"].split(",")],
        "events": [event.strip() for event in request.form["events"].split(",")],
        "similar_bookstores": []
    }

    # Make sure you call your similarity function here!
    new_store["similar_bookstores"] = suggest_similar_bookstores(new_store)

    bookstores.append(new_store)

    return jsonify({"success": True, "id": new_id})




if __name__ == "__main__":
    app.run(debug=True, port=5001)



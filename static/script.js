document.addEventListener("DOMContentLoaded", () => {
    // Fetch and display featured bookstores
    fetch("/api/featured")
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("featured-bookstores");
            container.innerHTML = ""; // Clear loading text

            data.forEach(bookstore => {
                const div = document.createElement("div");
                div.classList.add("col-md-4", "mb-4"); // 3 columns per row
            
                div.innerHTML = `
                    <div class="card shadow-sm h-100">
                        <a href="/view/${bookstore.id}" class="stretched-link">
                            <img src="${bookstore.image}" class="card-img-top" alt="${bookstore.title}">
                        </a>
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title">
                                <a href="/view/${bookstore.id}" class="text-decoration-none">${bookstore.title}</a>
                            </h5>
                            <p class="card-text flex-grow-1">${bookstore.summary.substring(0, 100)}...</p>
                        </div>
                    </div>
                `;
                container.appendChild(div);
            });
            
        })
        .catch(error => {
            console.error("Error fetching featured bookstores:", error);
            document.getElementById("featured-bookstores").innerHTML = "<p>Failed to load bookstores.</p>";
        });

    // Prevent search when input is only whitespace
    const searchForm = document.querySelector("nav form");
    const searchBox = document.getElementById("search-box");

    if (searchForm && searchBox) {
        searchForm.addEventListener("submit", (event) => {
            const query = searchBox.value.trim(); // Remove extra spaces

            if (query === "") {
                event.preventDefault(); // Stop form submission
                searchBox.focus(); // Keep the input focused
            }
        });
    }
});

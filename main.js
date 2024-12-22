document.getElementById("add-review-form").addEventListener("submit", function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const title = document.getElementById("title").value;
    const rating = document.getElementById("rating").value;
    const comment = document.getElementById("comment").value;

    fetch('/api/review', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            movie_id: window.location.pathname.split('/').pop(), // Dynamic movie ID
            user: username,
            title: title,
            rating: rating,
            comment: comment
        }),
    })
    .then(response => response.json())
    .then(data => {
        let date = new Date().toLocaleDateString();
        if (data.success) {
            // Add the new review to the page
            const newReview = `
                <div class="review-card">
                    <div class="review-header">
                        <h3 class="review-title">${data.review.title}</h3>
                        <span class="review-rating">⭐ ${data.review.rating}/10</span>
                    </div>
                    <p class="review-body">${data.review.body}</p>
                    <div class="review-footer">
                        <span class="review-author">${data.review.author}</span>
                        <span class="review-date">${date}</span>
                    </div>
                    <div class="review-actions">
                        <span class="helpful">👍 0</span>
                        <span class="not-helpful">👎 0</span>
                    </div>
                </div>`;

            document.querySelector(".reviews").innerHTML += newReview;
            document.getElementById("add-review-form").reset();

            // --- Redirect AFTER adding the review ---
            const movieId = window.location.pathname.split('/').pop();
            const movieDetailsUrl = `/movie/${movieId}`;
            window.location.href = movieDetailsUrl;
        } else {
            // Handle errors (e.g., display an error message)
            console.error("Failed to add review:", data.error);
        }
    })
    .catch(error => {
        // Handle fetch errors
        console.error("Fetch error:", error);
    });
});


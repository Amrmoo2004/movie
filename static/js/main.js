document.getElementById("add-review-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const movieId = window.location.pathname.split("/").pop();
    const formData = {
        user: document.getElementById("username").value,
        title: document.getElementById("title").value,
        rating: document.getElementById("rating").value,
        comment: document.getElementById("comment").value,
        movie_id: parseInt(movieId),
    };

    try {
        const response = await fetch("/api/review", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        });
        const result = await response.json();
        if (result.success) {
            alert("Review added successfully!");
            document.getElementById("add-review-form").reset();
            location.reload();
        } else {
            alert("Failed to add review: " + result.message);
        }
    } catch (error) {
        console.error("Error submitting review:", error);
        alert("An error occurred. Please try again later.");
    }
});

document.getElementById("add-to-watchlist").addEventListener("click", async () => {
    const movieId = window.location.pathname.split("/").pop();
    try {
        const response = await fetch(`/api/watchlist/${movieId}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
        });
        const result = await response.json();
        if (result.success) {
            alert("Movie added to your watchlist!");
        } else {
            alert("Failed to add movie to watchlist: " + result.message);
        }
    } catch (error) {
        console.error("Error adding to watchlist:", error);
        alert("An error occurred. Please try again later.");
    }
});

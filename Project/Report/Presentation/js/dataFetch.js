fetch("../Presentation/recommendations.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("recommendations").innerHTML = data;
        })
        .catch(error => {
            document.getElementById("recommendations").innerHTML = "<p>Error loading recommendations.</p>";
            console.error("Error fetching recommendations:", error);
        });
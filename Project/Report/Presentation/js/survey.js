let dataArray = JSON.parse(localStorage.getItem("energyData")) || [];

function displayResults() {
    let summaryDiv = document.getElementById("summary");
    summaryDiv.innerHTML = ""; 

    if (dataArray.length === 0) {
        summaryDiv.innerHTML = "<p>No data has been submitted yet.</p>";
        return;
    }

    dataArray.forEach(entry => {
        let entryDiv = document.createElement("div");
        entryDiv.classList.add("entry");
        entryDiv.innerHTML = `
            <p><strong>Country:</strong> ${entry.country}</p>
            <p><strong>Year:</strong> ${entry.year}</p>
            <p><strong>Renewable energy percentage:</strong> ${entry.renewablePercentage}%</p>
            <p><strong>Source:</strong> ${entry.source}</p>
            <hr>
        `;
        summaryDiv.appendChild(entryDiv);
    });
}

document.getElementById("energyForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let country = document.getElementById("country").value;
    let year = document.getElementById("year").value;
    let renewablePercentage = document.getElementById("renewablePercentage").value;
    let source = document.getElementById("source").value;

    if (country && year && renewablePercentage && source) {
        let formData = {
            country: country,
            year: parseInt(year),
            renewablePercentage: parseFloat(renewablePercentage),
            source: source
        };
        dataArray.push(formData);

        localStorage.setItem("energyData", JSON.stringify(dataArray));

        displayResults();

        document.getElementById("energyForm").reset();
    } else {
        alert("Complete all fialds.");
    }
});

document.getElementById("downloadButton").addEventListener("click", function () {
    if (dataArray.length === 0) {
        alert("No data for download. Input data first.");
        return;
    }
    const blob = new Blob([JSON.stringify(dataArray, null, 2)], { type: "application/json" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "data_renewable_energy.json";
    link.click();
});

window.onload = function () {
    displayResults();
};
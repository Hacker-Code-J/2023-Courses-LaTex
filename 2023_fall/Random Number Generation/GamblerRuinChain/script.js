const initialCapital = 5000000;
const winProbability = 0.1;
const goal = 10000000;
let currentCapital = initialCapital;
let isGambling = false; // To track if gambling is in progress

document.getElementById('startButton').addEventListener('click', function() {
    if (!isGambling) {
        currentCapital = initialCapital;
        isGambling = true;
        gamble();
    }
});

document.getElementById('resetButton').addEventListener('click', function() {
    currentCapital = initialCapital;
    isGambling = false;
    updateChart();
});

function gamble() {
    if (currentCapital === 0 || currentCapital >= goal || !isGambling) {
        isGambling = false;
        if (currentCapital >= goal) {
            document.getElementById('goalMessage').style.display = 'block'; // Show goal message
        }
        return;
    }

    if (Math.random() < winProbability) {
        currentCapital += 1000000;
    } else {
        currentCapital -= 100000;
    }

    updateChart();

    if (isGambling) {
        setTimeout(gamble, 100);
    }
}

// Modify the reset function to hide the message on reset
document.getElementById('resetButton').addEventListener('click', function() {
    currentCapital = initialCapital;
    isGambling = false;
    document.getElementById('goalMessage').style.display = 'none'; // Hide goal message
    updateChart();
});


function updateChart() {
    const chart = document.getElementById('chart');
    const widthPercent = (currentCapital / goal) * 100;
    chart.innerHTML = `<div class="bar" style="width: ${widthPercent}%;"></div>`;

    // Format currentCapital with commas
    document.getElementById('currentCapital').textContent = currentCapital.toLocaleString();
}
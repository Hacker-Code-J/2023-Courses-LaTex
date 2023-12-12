// script.js
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('randomWalkCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const resetButton = document.getElementById('resetButton');

    canvas.width = 600;
    canvas.height = 400;

    let isRunning = false;
    let positionX = canvas.width / 2;
    let positionY = canvas.height / 2;
    const startPositionX = positionX;
    const stepSize = 10;
    const delay = 500; // Delay in milliseconds before the particle disappears

    // Probabilities
    const p = 0.4; // Probability of moving right
    const q = 0.5; // Probability of moving left
    const r = 0.1; // Probability of staying in the same place

    function getNextStep() {
        const random = Math.random();
        if (random < p) {
            // Probability of moving right
            return 1;
        } else if (random < p + q) {
            // Probability of moving left
            return -1;
        } else {
            // Probability of staying in the same place
            return 0;
        }
    }
    

    function resetSimulation() {
        isRunning = false;
        startButton.textContent = 'Start Simulation';
        positionX = startPositionX;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function draw() {
        if (!isRunning) return;

        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous drawing
        const step = getNextStep();
        positionX += step * stepSize;

        ctx.beginPath();
        ctx.arc(positionX, positionY, 5, 0, 2 * Math.PI);
        ctx.fill();

        setTimeout(function() {
            if (isRunning) {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                requestAnimationFrame(draw);
            }
        }, delay);
    }

    startButton.addEventListener('click', function() {
        isRunning = !isRunning;
        if (isRunning) {
            startButton.textContent = 'Pause Simulation';
            draw();
        } else {
            startButton.textContent = 'Start Simulation';
        }
    });

    resetButton.addEventListener('click', resetSimulation);
});

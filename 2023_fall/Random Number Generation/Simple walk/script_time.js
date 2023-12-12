document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('randomWalkCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const resetButton = document.getElementById('resetButton');

    canvas.width = 600;
    canvas.height = 400;

    let isRunning = false;
    let time = 0; // Represents time on the x-axis
    let positionY = canvas.height / 2; // Represents the x-coordinate of the walk
    const startPositionY = positionY;
    const stepSize = 10;
    const delay = 500; // Delay in milliseconds for each step

    // Probabilities
    const p = 0.45; // Probability of moving right
    const q = 0.45; // Probability of moving left
    const r = 0.1; // Probability of staying in the same place

    function getNextStep() {
        const random = Math.random();
        if (random < p) {
            return 1;
        } else if (random < p + q) {
            return -1;
        } else {
            return 0;
        }
    }

    function resetSimulation() {
        isRunning = false;
        startButton.textContent = 'Start Simulation';
        time = 0;
        positionY = startPositionY;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function draw() {
        if (!isRunning) return;
    
        const step = getNextStep();
        positionY += step * stepSize;
    
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous drawing
    
        ctx.beginPath();
        ctx.arc(time, positionY, 5, 0, 2 * Math.PI);
        ctx.fill();
    
        // Increase time by a larger value to make it progress faster
        time += 64 * delay / 1000; // Double the rate of time progression
    
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

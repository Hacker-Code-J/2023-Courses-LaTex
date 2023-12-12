document.getElementById('visualizeBtn').addEventListener('click', function() {
    const bitstring = document.getElementById('bitstring').value;
    if (!/^[01]+$/.test(bitstring)) {
        alert("Please enter a valid bitstring consisting of 0s and 1s.");
        return;
    }

    const s = bitstring.split('').map(bit => parseInt(bit, 10));
    const N = s.length;
    const C_values = autocorrelation(s, N);

    // Create or update the chart
    updateChart(C_values);
});

function autocorrelation(s, N) {
    const C = new Array(N);
    for (let t = 1; t < N; t++) {
        let sum = 0;
        for (let i = 0; i < N; i++) {
            sum += (2 * s[i] - 1) * (2 * s[(i + t) % N] - 1);
        }
        C[t] = sum;
    }
    return C;
}

function updateChart(data) {
    const ctx = document.getElementById('autocorrelationChart').getContext('2d');
    if (window.myChart) {
        window.myChart.data.labels = [...Array(data.length).keys()];
        window.myChart.data.datasets[0].data = data;
        window.myChart.update();
    } else {
        window.myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [...Array(data.length).keys()],
                datasets: [{
                    label: 'Autocorrelation C(t)',
                    data: data,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}
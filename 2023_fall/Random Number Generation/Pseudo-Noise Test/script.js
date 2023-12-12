document.getElementById('verifyBtn').addEventListener('click', function() {
    const bitstring = document.getElementById('bitstringInput').value;
    if (!/^[01]+$/.test(bitstring)) {
        alert("Please enter a valid bitstring consisting of 0s and 1s.");
        return;
    }

    const results = verifyGolombsPostulates(bitstring);

    displayTestResult("testR1", "Test R1: ", results.testR1);
    displayTestResult("testR2", "Test R2: ", results.testR2);
    displayTestResult("testR3", "Test R3: ", results.testR3);
});

function verifyGolombsPostulates(bitstring) {
    const N = bitstring.length;

    // Test R1: Balance Property
    const onesCount = bitstring.split('1').length - 1;
    const zerosCount = N - onesCount;
    const balanceProperty = Math.abs(onesCount - zerosCount) <= 1;

    // Test R2: Run Distribution
    const runs = countRuns(bitstring);
    const runDistribution = verifyRunDistribution(runs, N);

    // Test R3: Autocorrelation Property
    const autocorrelationProperty = verifyAutocorrelation(bitstring, N);

    return { testR1: balanceProperty, testR2: runDistribution, testR3: autocorrelationProperty };
}

function countRuns(bitstring) {
    const runs = { '0': {}, '1': {} };
    let currentRun = 1;
    let currentType = bitstring[0];

    for (let i = 1; i < bitstring.length; i++) {
        if (bitstring[i] === currentType) {
            currentRun++;
        } else {
            if (runs[currentType][currentRun]) {
                runs[currentType][currentRun]++;
            } else {
                runs[currentType][currentRun] = 1;
            }
            currentRun = 1;
            currentType = bitstring[i];
        }
    }

    if (runs[currentType][currentRun]) {
        runs[currentType][currentRun]++;
    } else {
        runs[currentType][currentRun] = 1;
    }

    return runs;
}

function verifyRunDistribution(runs, N) {
    let minRunLength = 1;
    let runDistribution = true;
    let totalCount = 0;

    for (let l = 1; l < N; l++) {
        const requiredRuns = totalCount / (2 ** l);
        if (requiredRuns <= 1) {
            break;
        }
        const actualRuns = (runs['0'][l] || 0) + (runs['1'][l] || 0);
        runDistribution &= actualRuns >= requiredRuns;
        runDistribution &= Math.abs((runs['0'][l] || 0) - (runs['1'][l] || 0)) <= 1;
        totalCount += actualRuns;
    }

    return runDistribution && totalCount > 1;
}

function verifyAutocorrelation(bitstring, N) {
    function autocorrelation(t) {
        let sumProduct = 0;
        for (let i = 0; i < N; i++) {
            sumProduct += (2 * parseInt(bitstring[i]) - 1) * (2 * parseInt(bitstring[(i + t) % N]) - 1);
        }
        return sumProduct / N;
    }

    let autocorrelationProperty = true;
    for (let t = 1; t < N; t++) {
        if (autocorrelation(t) !== -1 / N) {
            autocorrelationProperty = false;
            break;
        }
    }

    return autocorrelationProperty;
}

function displayTestResult(id, label, passed) {
    const resultElement = document.getElementById(id);
    resultElement.textContent = label + (passed ? "Passed" : "Failed");
    resultElement.classList.remove("passed", "failed");
    resultElement.classList.add(passed ? "passed" : "failed");
}

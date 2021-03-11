
// calculates a list for each divisor of every dividend up through the dividend limit that each divisor up to the divisor limit is a factor of

// "divisorLimit" represents highest divisor to test...
// "dividendLimit" represents highest dividend to test...
// "divisor" represents the divisor...
// "dividend" represents the dividend...
// each element in "results" will list the numbers that the current divisor is a factor of...
function godNumFactors(divisorLimit, dividendLimit, divisor = 0, results = []) {
    // base case divisor of 0:
    if (divisor === 0) {
        results.push("0 is only a factor of itself!");
        divisor++;
        godNumFactors(divisorLimit, dividendLimit, divisor, results);
    // base case divisor of 1:
    } else if (divisor === 1) {
        results.push("1 is a factor of everything!")
        divisor++;
        godNumFactors(divisorLimit, dividendLimit, divisor, results);
    // everything else:
    } else {
        for (divisor; divisor <= divisorLimit; divisor++) {
            results[divisor] = `${divisor} is a factor of: `;
            // dividend tests to start at 1 b/c 0 is already covered above arbitrarily...
            for (dividend = 1; dividend <= dividendLimit; dividend++)
                if (dividend % divisor === 0)
                    results[divisor] += `${dividend}/`;
        }
        // print the results!
        for (factor of results) {
            console.log("***********");
            console.log(factor);
            console.log("***********");
        }
    }
    // return the results
    return results;
}

// godNumFactors(5, 100);

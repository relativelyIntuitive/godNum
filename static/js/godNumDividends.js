
// finds all numbers up through a dividend limit that are divisible by every number up through a divisor limit...

// "dividendLimit" represents the highest dividend to test...
// "divisorLimit" represents the highest divisor to test...
function godNumDividends(dividendLimit, divisorLimit) {
    // declare variables...
    let dividends = [];
    let results = "";

    // test each dividend up through the limit
    for (dividend = 1; dividend <= dividendLimit; dividend++) {
        let isCommonDividend = false
        for(divisor = 1; divisor <= divisorLimit; divisor++) {
            if (dividend % divisor === 0 && divisor === divisorLimit && isCommonDividend === true) {
                isCommonDividend = true;
                dividends.push(dividend);
            } else if (dividend % divisor === 0){
                isCommonDividend = true;
            } else {
                isCommonDividend = false;
                break;
            }
        }
    }

    // compile the results
    if (dividends.length === 0) {
        results = `No dividends up through ${dividendLimit} are divisible by every number up through ${divisorLimit}!`;
    } else if (dividends.length === 1) {
        results = `${dividends[0]} is the only number up through ${dividendLimit} divisible by every number up through ${divisorLimit}!`;
    } else if (dividends.length === 2) {
        results = `${dividends[0]} and ${dividends[1]} are the only numbers up through ${dividendLimit} divisible by every number up through ${dividendLimit}!`;
    } else{
        for (i = 0; i < dividends.length - 1; i++) {
            results += `${dividends[i]},\n`;
        }
        results += `${dividends[dividends.length - 2]}\n and ${dividends[dividends.length - 1]} are the only numbers up through ${dividendLimit} divisible by every number up through ${divisorLimit}!`;
    }

    // print and return the results!
    console.log('***********');
    console.log(results);
    console.log('***********');
    return results;
}

// godNumDividends(100, 5);
// 5.309 seconds...not bad

// godNumDividends(9999999999, 12);
// 285.416 seconds...massive difference...

// godNumDividends(10000000000, 12);
// ??? seconds...difference of 1 has such an impact?...11 digit number issue?

// godNumDividends(10000000000, 1);
// 145.205 seconds...11 digit number issue...

// godNumDividends(9999999999, 1);
// 144.787 seconds...not as bad as divisorLimit of 12...

// godNumDividends(1, 1000000000);
// 0.212 seconds...dividends take longer to test?

// godNumDividends(1, 1000000000000000000000);
// 0.216 seconds...wow...why dividend test? more intense than divisor tests?
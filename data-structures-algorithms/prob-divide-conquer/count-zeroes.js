function countZeroes() {
    let count = 0;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            count++;
        } else {
            break;
        }
    }

    return count;
}

module.exports = countZeroes
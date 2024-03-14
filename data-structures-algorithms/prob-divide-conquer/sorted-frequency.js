function sortedFrequency(arr, num) {
    let firstIdx = findFirst(arr, num);
    if (firstIdx == -1) return firstIdx;
    let lastIdx = findLast(arr, num);
    return lastIdx - firstIdx +1;
}

function findFirst(arr, num, low = 0, high = arr.length -1) {
    if ()
}

module.exports = sortedFrequency
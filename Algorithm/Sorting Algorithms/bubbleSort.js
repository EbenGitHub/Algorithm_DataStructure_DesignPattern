// WorestCase Time Complexity: O(n^2)
// BestCase Time Complexity: O(n)
// Average Time Complexity: O(n^2)
// Space Complexity: O(1)

function bubbleSort(arr) {
    let isSorted = false
    while (!isSorted) {
        isSorted = true
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                isSorted = false
                let tempVar = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tempVar
            }
        }
    }
    return arr
}

let output = bubbleSort([2, 3, 3, 1, 3, 4, 2, 4, 3, 3])
console.log(output)
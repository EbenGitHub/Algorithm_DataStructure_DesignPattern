// WorestCase Time Complexity: O(n^2)
// BestCase Time Complexity: O(n)
// Average Time Complexity: O(n^2)
// Space Complexity: O(1)

function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let current = arr[i]
        let j = i - 1
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j]
            j--
        }
        arr[j + 1] = current
    }
    return arr
}

let output = insertionSort([5, 4, 3, 2, 32, 3, 3, 2, 1, 1])
console.log(output)
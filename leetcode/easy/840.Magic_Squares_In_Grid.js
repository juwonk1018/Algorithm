
function getGridSize(arr) {
    const width = arr[0].length;
    const height = arr.length;

    return {width, height}
}

function sum(arr) {
    return arr.reduce((acc, cur) => acc + cur, 0);
}

function isMagicSquare(grid, x, y, size) {
    const {width, height} = getGridSize(grid)

    if(x + size > height || y + size > width) return false;

    let targetSum = 0;


    
    // Row Sums Check
    for(let row = x; row < x+size; row++) {
        const rangeSum = sum(grid[row].slice(y, y+size));

        if(targetSum === 0){
            targetSum = rangeSum; // initialize, if not.
        } else if(targetSum !== rangeSum){
            return false;
        }
    }

    // Column Sums Check
    for(let col = y; col < y+size; col++) {
        let rangeSum = 0;
        for(let i=0; i < size; i++){
            rangeSum += grid[x+i][col];
        }

        if(targetSum !== rangeSum){
            return false;
       }
    }


    // Diagnoal Sums Check 1
    let diag1 = 0;
    for(let i = 0; i < size; i++){
        diag1 += grid[x+i][y+i];
    }

    if(targetSum !== diag1){
        return false;
    }
    

    // Diagnoal Sums Check 2
    let diag2 = 0;
    for(let i = size - 1; i >= 0; i--){
        diag2 += grid[x+size-1-i][y+i]
    }

    if(targetSum !== diag2){
        return false;
    }

    return true;
}

/**
 * @param {number[][]} grid
 * @return {number}
 */


var largestMagicSquare = function(grid) {
    let answer = 1;

    const { width, height } = getGridSize(grid);

    for(let i = 0; i < height; i++){
        for(let j = 0; j < width; j++){
            for(let size = 2; j + size <= width && i + size <= height; size++) {
                if(isMagicSquare(grid, i,j,size)){
                    answer = Math.max(size, answer);
                }
            }
        }
    }

    return answer;
};
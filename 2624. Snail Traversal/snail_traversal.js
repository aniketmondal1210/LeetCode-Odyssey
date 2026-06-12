/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return [];
    }

    const matrix = Array.from({ length: rowsCount }, () => Array(colsCount));
    
    let row = 0;
    let col = 0;
    let direction = 1;

    for (let i = 0; i < this.length; i++) {
        matrix[row][col] = this[i];
        row += direction;

        if (row === rowsCount) {
            row = rowsCount - 1;
            direction = -1;
            col++;
        } else if (row === -1) {
            row = 0;
            direction = 1;
            col++;
        }
    }

    return matrix;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */

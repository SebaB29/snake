function toKey(x, y) {
    return `${x},${y}`;
}

function buildSet(items) {
    return new Set((items || []).map((item) => toKey(item.x, item.y)));
}

export default function Board({ board, snake, fruit, obstacles }) {
    const rows = board?.rows ?? 21;
    const columns = board?.columns ?? 21;
    const snakeCells = snake || [];
    const fruitCells = fruit || [];
    const obstacleCells = obstacles || [];
    const snakeSet = buildSet(snakeCells);
    const fruitSet = buildSet(fruitCells);
    const obstacleSet = buildSet(obstacleCells);
    const head = snakeCells.length ? snakeCells[snakeCells.length - 1] : null;

    const cells = [];
    for (let y = 0; y < rows; y += 1) {
        for (let x = 0; x < columns; x += 1) {
            const key = toKey(x, y);
            let className = "cell";

            if (head && head.x === x && head.y === y) {
                className += " snake head";
            } else if (snakeSet.has(key)) {
                className += " snake";
            } else if (fruitSet.has(key)) {
                className += " fruit";
            } else if (obstacleSet.has(key)) {
                className += " obstacle";
            }

            cells.push(<div className={className} key={key} />);
        }
    }

    return (
        <div className="board-grid" style={{ "--rows": rows, "--cols": columns }}>
            {cells}
        </div>
    );
}

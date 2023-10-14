function validPath(n, edges, source, destination) {
    const graph = new Map();

    for (let i = 0; i < n; i++) {
        graph.set(i, []);
    }

    for (const [x, y] of edges) {
        graph.get(x).push(y);
        graph.get(y).push(x);
    }

    let visited = new Set();

    function dfs(node) {
        if (node === destination) {
            valid = true;
            return;
        }

        visited.add(node);

        for (const neighbor of graph.get(node)) {
            if (!visited.has(neighbor)) {
                dfs(neighbor);
            }
        }
    }

    let valid = false;
    dfs(source);

    return valid;
}



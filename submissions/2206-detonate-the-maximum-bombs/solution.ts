function maximumDetonation(bombs: number[][]): number {
  const n = bombs.length;

  const graph = Array(n).fill(0).map(() => []);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i !== j) {
        const [xi, yi, ri] = bombs[i];
        const [xj, yj] = bombs[j];

        const distance = Math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2);

        if (distance <= ri) {
          graph[i].push(j);
        }
      }
    }
  }

  function bfs(start: number): number {
    const visited = Array(n).fill(false);
    const queue = [start];
    visited[start] = true;
    let detonated = 0;

    while (queue.length > 0) {
      const current = queue.shift()!;
      detonated++;

      for (const neighbor of graph[current]) {
        if (!visited[neighbor]) {
          queue.push(neighbor);
          visited[neighbor] = true;
        }
      }
    }

    return detonated;
  }

  let maxDetonations = 0;

  for (let i = 0; i < n; i++) {
    maxDetonations = Math.max(maxDetonations, bfs(i));
  }

  return maxDetonations;
}


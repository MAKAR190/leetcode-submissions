function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
  if (
    !wordList.includes(endWord) ||
    !endWord ||
    !beginWord ||
    wordList.length === 0
  ) {
    return 0;
  }

  const L = beginWord.length;

  const allComboDict: Record<string, string[]> = {};
  wordList.forEach((word) => {
    for (let i = 0; i < L; i++) {
      const genericWord = word.slice(0, i) + '*' + word.slice(i + 1);
      if (allComboDict[genericWord]) {
        allComboDict[genericWord].push(word);
      } else {
        allComboDict[genericWord] = [word];
      }
    }
  });

  const queue: [string, number][] = [[beginWord, 1]];
  const visited: Record<string, boolean> = {};
  visited[beginWord] = true;

  while (queue.length > 0) {
    const [currentWord, level] = queue.shift()!;

    for (let i = 0; i < L; i++) {
      const intermediateWord = currentWord.slice(0, i) + '*' + currentWord.slice(i + 1);

      for (const word of allComboDict[intermediateWord] || []) {
        if (word === endWord) {
          return level + 1;
        }

        if (!visited[word]) {
          visited[word] = true;
          queue.push([word, level + 1]);
        }

        allComboDict[intermediateWord] = [];
      }
    }
  }

  return 0;
}


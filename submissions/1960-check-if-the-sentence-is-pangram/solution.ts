function checkIfPangram(sentence: string): boolean {
  const result = new Set([...sentence]);
  return Array.from(result).length === 26; 
};

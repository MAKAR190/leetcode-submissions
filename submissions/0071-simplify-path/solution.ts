function simplifyPath(path: string): string {
  const parts = path.split('/');
  const stack = [];

  for (const part of parts) {
    if (part === '..') {
      stack.pop();
    } else if (part !== '' && part !== '.') {
      stack.push(part);
    }
  }

  return '/' + stack.join('/');
}


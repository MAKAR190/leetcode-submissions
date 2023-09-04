function makeGood(s: string): string {
  let result = [];

    for (let i = 0; i < s.length; i++) {
        const current = s[i];
        const last = result.length ? result[result.length - 1] : '';

        if (current.toLowerCase() === last.toLowerCase() && current !== last) {
            result.pop();
            continue;
        }

        result.push(current);
    }

    return result.join('');
};

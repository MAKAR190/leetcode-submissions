function findMaxLength(nums: number[]): number {
    let maxLength = 0;
    let count = 0;
    const countMap = new Map<number, number>();

    countMap.set(0, -1);

    for (let i = 0; i < nums.length; i++) {
        // Increment or decrement count
        count += nums[i] === 1 ? 1 : -1;

        // Check if this count has been seen before
        if (countMap.has(count)) {
            // Calculate the length of the subarray
            const prevIndex = countMap.get(count)!;
            maxLength = Math.max(maxLength, i - prevIndex);
        } else {
            // Store the first occurrence of this count with its index
            countMap.set(count, i);
        }
    }

    return maxLength;
}


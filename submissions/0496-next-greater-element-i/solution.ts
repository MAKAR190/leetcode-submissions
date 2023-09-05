function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    const stack: number[] = [];
        const map: Map<number, number> = new Map<number, number>();

        for (let i = 0; i < nums2.length; i++) {
            while (stack.length > 0 && nums2[i] > stack[stack.length - 1]) {
                map.set(stack.pop() as number, nums2[i]);
            }
            stack.push(nums2[i]);
        }

        while (stack.length > 0) {
            map.set(stack.pop() as number, -1);
        }

        const res: number[] = [];
        for (let i = 0; i < nums1.length; i++) {
            res.push(map.get(nums1[i]) as number);
        }

        return res;
    }

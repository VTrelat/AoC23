import * as fs from "fs";
const data = fs.readFileSync("/Users/vincent/Documents/AoC23/inputs/input3.txt", { encoding: "utf-8", flag: "r" }).trim().split("\n");

import * as perf from "perf_hooks";

const startTime = perf.performance.now();
let part1 = 0;
let part2 = 0;

const isNumberInRange = (number, min, max) => number >= min && number <= max;

const numbersList = data.flatMap((item, y) => {
    let indexOffset = 0;
    return item.match(/\d+/g).map((num) => {
        let index = item.indexOf(num, indexOffset);
        indexOffset = index + num.length;
        return { x: index, y, length: num.length, num: +num, used: false };
    });
});

data.forEach((item, y) => {
    [...item].forEach((char, x) => {
        let charList = [];
        if (/[^0-9.]/.test(char)) {
            numbersList.filter((v) => {
                const valid = isNumberInRange(x, v.x - 1, v.x + v.length) && isNumberInRange(v.y, y - 1, y + 1) && !v.used;
                valid && (v.used = true);
                char == "*" && valid && charList.push(v.num);
                return valid;
            });
        }
        if (charList.length == 2) {
            part2 += charList[0] * charList[1];
        }
    });
});

part1 = numbersList.reduce((sum, obj) => (obj.used ? sum + obj.num : sum), 0);
const time = perf.performance.now() - startTime;
console.log(`Part 1: ${part1}\nPart 2: ${part2}\nTimer: ${time} ms`);

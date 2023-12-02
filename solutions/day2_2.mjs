import * as fs from "fs";
const data = fs
    .readFileSync("/Users/vincent/Documents/AoC23/inputs/input2.txt", { encoding: "utf-8", flag: "r" })
    .trim()
    .split("\n")
    .map((line) => line.split(": "))
    .map((line) =>
        Object.values(
            line[1]
                .split(";")
                .map((l) =>
                    l
                        .split(", ")
                        .map((l) => {
                            let t = l.trim().split(" ");
                            return { [t[1]]: parseInt(t[0]) };
                        })
                        .reduce((acc, cur) => ({ ...acc, ...cur }), {})
                )
                .reduce((result, item) => {
                    Object.entries(item).forEach(([key, value]) => {
                        result[key] = Math.max(value, result[key] || 0);
                    });
                    return result;
                }, {})
        ).reduce((acc, cur) => acc * cur, 1)
    )
    .reduce((acc, cur) => acc + cur, 0);

console.log(data);

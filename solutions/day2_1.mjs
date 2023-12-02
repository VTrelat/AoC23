import * as fs from "fs";
const data = fs
    .readFileSync("/Users/vincent/Documents/AoC23/inputs/input2.txt", { encoding: "utf-8", flag: "r" })
    .trim()
    .split("\n")
    .map((line) => line.split(": "))
    .map((line) => [
        parseInt(line[0].split(" ")[1]),
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
            .map((l) => {
                if (l["red"]) {
                    l["red"] -= 12;
                }
                if (l["green"]) {
                    l["green"] -= 13;
                }
                if (l["blue"]) {
                    l["blue"] -= 14;
                }
                return l;
            })
            .map((l) => Object.values(l).map((l) => l <= 0))
            .flat()
            .reduce((acc, cur) => acc && cur, true),
    ])
    .filter((line) => line[1])
    .map((line) => line[0])
    .reduce((acc, cur) => acc + cur, 0);

console.log(data);

const fsLibrary = require('fs');

const input = fsLibrary.readFileSync('/Users/jose/Code/JoseCanHelp/advent-of-code/test.txt', 'utf8').split(/\n{2,}/g)

// const part1 = input.reduce((count, group) => {
//     return count + new Set(group.split('').filter(n => n != '\n')).size
// }, 0)

// console.log(part1)

const intersect = (i, j) => {
    return new Set([...new Set(i)].filter(x => new Set(j).has(x)))
}

z = input.map(i => i.split('\n').map(y => y.split()))

console.log(z)
console.log(z.map(b => new Set(b.filter(n => n != ''))))
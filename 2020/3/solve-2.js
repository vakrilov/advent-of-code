const arr = [
  ".#....#..##.#..####....#.......",
  "......#..#....#....###......#.#",
  "#..#.....#..............##.#.#.",
  "#.#...#....#...#......##..#..#.",
  "...#..#.##..#..#........###.#.#",
  "...#.#..........#.........##...",
  "...#.#....#.#....#..#......#...",
  "..##.#.....#.......#.###..#..##",
  "..#.......#.......#....##......",
  "....##........##.##...#.###.##.",
  "#.......#.......##..#......#...",
  "..##.............##.#......#...",
  "...#.####....#.....#...##......",
  ".............##.#......#.......",
  "..#...#....#......#....#.......",
  "..#....#..#............#.......",
  "##...#..#........##..#......#..",
  "##........##........#.#.......#",
  "#.......#........#.#..#....###.",
  ".....#..#.#..........##...#....",
  "..##...#......#.#...#..#...#...",
  "##.##...#......#....#....#...#.",
  "#.......#..#.#..#....#..###.#.#",
  "#.............#.#....#..#.#....",
  "...#.......###.#.##.##.#...#..#",
  ".##.......##..##...#..###......",
  ".......#.#.#.#..####..#..#..#..",
  "...##......#.#.##.###....#.###.",
  "###......###......#.#####..#...",
  "..#........##..#..##.##..#...#.",
  ".....##..#...#..#.##.....#.#...",
  "#......#.##....#..##.#....#.#..",
  "##.#.##..#................#....",
  "......#.#....#......##.....#...",
  "..#...##..#..#...#..#.#..#.....",
  "........#.#.#.##...#.#.....#.#.",
  "#.#......#.....##..#...#.......",
  "..#.#......#...........###.....",
  "......##....#....##..#..#.#.#.#",
  "##....#.###...#......#..#...#..",
  "#.#.##....###...####.......#..#",
  "##...........#.....#........#.#",
  ".##.#..#.....#......#.......#..",
  "##..##..###....#.........##....",
  "..#..#..#.##...#.#...#........#",
  "#.##.###...#.......#...........",
  ".........#.................#...",
  "#.##...#.....#..##........#....",
  "....#.#...##...#...........#...",
  ".#.....#.#..#...##..##.....#...",
  ".#.....####....#..##..#........",
  "...#..#......##.#..##.#.#.#..#.",
  ".##.#.....#.....#...#.......##.",
  "......#..#..#......#...####....",
  ".......#......##..#..##.....#..",
  "......#.#..#...#..#.#..........",
  "....##.........#...............",
  ".#....#..##.....#....##.##.....",
  "#.#.....#...#....####....#.#...",
  "#.....#....#.#...#.............",
  "...#..#.....#....##..#..#......",
  "...#.#............#...........#",
  "###.#..#.#......#.....##.....#.",
  "####....#....###.....#..#.#####",
  ".###..#...#.#..#......##.#.#.#.",
  ".....#.##.#....#..##....#..#..#",
  "...#....#...##.....#......#.#..",
  "....#...#....#...#....#.....#.#",
  ".#.....#.....#.#..#......#..#..",
  "..#..##....##.##....#.....##...",
  "#..##...#.##...#..#.#.#.....#..",
  "...#..##.#..#....#.#....######.",
  "..........#..#.....#....#...##.",
  "#.#####.#.###..#.....#.........",
  "#....#......#..#.#.##.##..###..",
  "..#...###.#.#....##.##...##....",
  ".......#....#..#...##......#...",
  "...#.#...#..#.....#..##.#......",
  "###..##...........#............",
  "..#....#.##....#.#..##...#.....",
  "##....#...#....#.....#.#..##...",
  "..............#.##.#..#..##.###",
  "......#..#..#..#.#....###...##.",
  ".#...#..#.#.#....#..........#..",
  "..#.#.....#..#...........#.##..",
  "...#.#......#......#..#..#.#...",
  "...#....#.#.#.....#...#.##..#..",
  ".#.#..#...#........##.......#..",
  "##..........#..#...#....###.#..",
  "#.....###......#..#.#.#....#.#.",
  "..###.......#.#...............#",
  "#....#.....#.#......#..##.##...",
  "#.##.#.#....#..#.#...#.#...#..#",
  "#....#..#...........#.......#..",
  "...#.####.....#.........###.##.",
  "......#..#.....#..........#..#.",
  "#...#.#..####...#...#.#.##...##",
  ".##.........#......#.#.#.......",
  ".......##...##.##....###...##..",
  "...#..#....#..#.#.#.....#.#....",
  "#....#.#.#.......##..###..##...",
  "......#............#.#...#..#..",
  "#.#.....#......#...#.......###.",
  "...#.#................#...#....",
  ".....#......#.#..#...##.#.#...#",
  "#....#.#..#..#..##..#.##..#....",
  "#.................#..#....#....",
  "..#....#.......####....###.....",
  ".#..#.#.#...###..#...#..###....",
  "..#..#.#......#.###..........#.",
  ".....#......#.......##....##.#.",
  ".#....#........#.#.##.#........",
  "#.#..##..#..#.#...####....##...",
  "...#....#.#..#...#..........#..",
  ".#.....#.##....#...##..........",
  "....##....#.....#.....#...#.###",
  ".#...##.#.#..##..#...#.#..#..#.",
  "..#.......#.##.....#.#........#",
  "...#...#.....##..#.#.#....#....",
  "...#.....#.......##.........#.#",
  ".##.....#..#.#...#.#...#.#...#.",
  "...........#...#.###..#...#..#.",
  "#.##........#..###.##...####...",
  ".#.....#.#...##...#..#..#...##.",
  "..#....#..#...#.....#.....##...",
  "..###..#.#.....##........#.##..",
  ".#.#..##........#.##....#..#.##",
  ".####.#..##..#.#..#....##....#.",
  ".##....##...#.#........#.......",
  "....#..#..#...#..#..#..#.#.....",
  "...#......................#....",
  "#.....#.#....#..#..#.#..#....#.",
  "##.....#.....##..........###...",
  ".#..#..............#...##.#.#.#",
  "...#...#.#.............#.#..#.#",
  "..#.....#.......#......#.#.....",
  ".###.#..#..#..#.#..#.....#.....",
  ".....##..##...##.......#....###",
  ".#........###...##..#....##....",
  "#....#.#......##..#....#.##..#.",
  "#....#.#...#........##...###...",
  ".#.....#...#.###....#.##.#.####",
  "###......#....#...#....##..#..#",
  "##....#..###......#...#.#.#....",
  "..........#......##.#..#.......",
  ".#..#......###.........##...#..",
  "....#......#....#.........#.#.#",
  "##.#.#...#.#...#...#..#......#.",
  "....#.##.........#..#.....##.#.",
  "........#...#..#.#.#.#.....##..",
  "..#......#.#.#..#.....##.......",
  "..............#....#....##.#..#",
  "....#.#.....#....#.#.###.#....#",
  "..#..........#..#......#.##..#.",
  "...#...#.#.............#..#....",
  "#.......#..#..##.........##..#.",
  "..##..#............#.....#.....",
  "....#.#..##...#.#..#.........#.",
  "........#.......#.##....#....#.",
  "...#.....#.#.....#.#....#......",
  "..#......##.#.............#.#.#",
  "#.#.............#.#.....#......",
  ".##....##.#.....#....#...##....",
  ".#.#....##....#.....##.........",
  "...#.....#.....#.....#..#.###..",
  ".......#....#...##.#...#...#..#",
  "..#.#.......#...###.#...#....#.",
  ".....###..##....###.#.##.......",
  "....#..................##.#.##.",
  ".#.......###.##...#.#.....#....",
  "....#....##...##.....#.#...#..#",
  "#..#.....#......##...#....#....",
  "#..##.........#.....#...#......",
  "...#..##.......##......#..#####",
  ".#..###.###.#.##........#......",
  ".#...#....#....#.#....#...##...",
  "##........#....#.........##..#.",
  ".#.....##............#.#.......",
  "....#....#...........###.....##",
  ".#......#.#.#..#....#.#.....##.",
  "......#.##.#..##....#.#.#..#...",
  "#....#......#...#..####........",
  "......#..#..##..#.......#.#..#.",
  "##....##.###.#...#.##.#..#.###.",
  ".#.........#...##...#.#......#.",
  "..#.#...........####.#....##.##",
  ".....#.#..##.#...###...#..#.#..",
  "...#..#..##.#...#.....#.##...##",
  "..##......##..........#..###...",
  ".#......##.....#.##....#.#.##.#",
  "...#.......##..##.....#....#...",
  ".##...#...#....#..#............",
  "#..#....#...........#..........",
  "......#...#.#.......#...#.##..#",
  "..#.###..#.....#.....#..#.....#",
  "....#....#..........##....#..#.",
  ".......##.#.#.#......#....#...#",
  "####..#.###........#..#......#.",
  "#........##.#.#.#.............#",
  ".#......#......#..#.##.....#...",
  ".....##.##......##.#.....#.#.#.",
  ".......##.#.....##.......#.#.#.",
  ".#.#..#.#..#.##...#.#....#.#..#",
  ".#..##....#..#...##.......#..#.",
  ".#.#..#.......#................",
  "#........#.#.#......#.#.#.#....",
  "##......#...#..##.#...##.##....",
  "##.#..#...........##...#..###..",
  "......#.####...#........#.#.#..",
  "...#........##..###.#.#...#...#",
  ".#.....##..#......##......###..",
  "..#.#...#......#..#..##.#.....#",
  "#....#..#.#..........#...#.....",
  ".#......#.##..###..#.#....#..##",
  ".......#.......#..#..#......#..",
  "..##.....##.#..#..#.....##.....",
  "........#.##...#.#.#..#..#..#..",
  "...#.######.........#.....#..##",
  ".#.#............#....#.........",
  "#...#....###.#......#.#........",
  "#.........#....#...##..........",
  "....#...........#.###.#...###..",
  ".........#........#.#.#..#...#.",
  ".#.......#.#.....#.#.....#.##..",
  ".....#.......#.....#.#.#.......",
  "#.##..#..##.......#...#......#.",
  ".###.....##...##.#...##.##.#.#.",
  "...#......##..##............#.#",
  "...#......................#..##",
  "#..#..#................#...#...",
  "#..#....#.#.#...##.......#..#..",
  "....#.#..###.##...#..#.###..#..",
  "..#...#....####.#............#.",
  "......#....#.#...#.#.#.........",
  "#...#........#.....##..###.#..#",
  "#....#...#...##...#..#....##...",
  "#..#...#..#.......#.#..##.#..#.",
  "#.#..........#...........##....",
  ".#...###...#......#.......#.#.#",
  ".........#.........#...#...##..",
  "##.#..###......##..#.....#..#..",
  "....##...............#.....#...",
  ".....#.....###.#.....#.#.......",
  "....#..#......###..#..##..#....",
  "......................#.....#..",
  "..#..#...##....##....#........#",
  "..#....#...#...#.......#.....#.",
  "...##.#.#.##......#.#.#.#.####.",
  ".###...#..#......#.#..#........",
  "#..#...##.#..#..##..##....#...#",
  "...#...#..#..#..#........#..##.",
  ".##....#.##.#....#...#.#.#....#",
  "#..#....#..#....#.......##..#.#",
  "...#.#....####...........#...#.",
  "#...#####...#.#..#......#...#.#",
  ".##....#.#.#..#......#..##.....",
  "..........#..#.#.#.....##......",
  ".....#....#..................#.",
  ".........#...#...#....#..###...",
  ".#.#.#....#....................",
  "......##............##.###..#..",
  "#.#...#........####.##..#.#.##.",
  "#........#.#.#.#..#.##.....#...",
  "......####..#.##.......#....#..",
  ".........#...#...#.....#.......",
  "..##.....#...#...#.....##.....#",
  "....#...##....#.....#..#..##.##",
  "..#.........##...##..###..#....",
  "#....#.#.........##.###.#...##.",
  ".##...#....#..#..#.#....##.....",
  "##..#..#..#...........#.##....#",
  "....#..........#...#..#.....#..",
  "........###..#..#.#.#.....##...",
  "#...#...#..###............###..",
  "..#.....#.#.#..#..#.#..#......#",
  "..#...##..#....#...#......#....",
  "#....#........##.....#..##....#",
  "#.....#.#.#..#.......##.#.#.##.",
  "..##...#...#.....#..........#..",
  "##.....#....#......#..........#",
  "......#..#..........#.#..####..",
  "......#...#............##...##.",
  "..#.......##.......#...###.###.",
  ".#..#.#.#...#..##.#......#.#...",
  ".##.....##.#.#...#.##.........#",
  "#.#.######...........#.#####.#.",
  "........#.##...##....##.#.##.#.",
  "....#......#.....#.....###...##",
  "#..............#.#....#.#....#.",
  "....#..###.#.........##.#.#....",
  "..#.#.#..##....####..........#.",
  "...#..#.......#................",
  "...#....#..............#....#..",
  ".....#...#...#....#.#.#..#...#.",
  "......##.............###.##..##",
  ".#...#.#..#......#..#.##.......",
  "##.....#.....#.##...#....#.....",
  "..#..#.#.#.#.#..........#..###.",
  "##..........#........#....#.#..",
  ".....#...#........#.#..###....#",
  ".###.#........#.##......#.#...#",
  "#...##....#....#....##.#.#.....",
  ".....#.#............#..........",
  "..#.##....................#....",
  ".....#..#..#.#..#.##.......#...",
  ".....###......#......##......##",
  "#.....#.#.......##.......#...#.",
  ".#.#...#......#..###...#.....#.",
  "#.#..#...#..##.....#...#.#..#..",
  ".....#.#..........#..#.........",
  ".###..##..##.....#...#...#..##.",
  "#...#.#....#.......##..#.......",
  "###...#.#.#..#.......#......#..",
  "....##........#..........##....",
  "............#....#...........#.",
  "#..#.#....##..#.#..#......##...",
  ".###....##...#....##..........#",
  ".###........#........###.....#.",
  "...#...#.#......#...#....#.....",
  ".###.......#.........#.........",
  "....##.#......#...###......##.#",
  ".###...#..##.....##.......#....",
  ".#.#...#..#.##....#........#...",
];

const patternLen = arr[0].length;
function solve(down, right) {
  let result = 0;

  for (let i = 0; i < arr.length; i += down) {
    if (arr[i][(i * right / down) % patternLen] === "#") result++;
  }

  return result;
}

const res = solve(1, 1) * solve(1, 3) * solve(1, 5) * solve(1, 7) * solve(2, 1);

console.log(solve(1, 1));
console.log(solve(1, 3));
console.log(solve(1, 5));
console.log(solve(1, 7));
console.log(solve(2, 1));
console.log(res);

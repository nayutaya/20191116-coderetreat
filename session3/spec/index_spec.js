
const index = require("../index");

describe("自分の状態と隣接する生きているセルの数から次の状態を決定する", () => {
  it("", () => {
    expect(index.isAlive(true, 0)).toBe(false);
    expect(index.isAlive(true, 1)).toBe(false);
    expect(index.isAlive(true, 2)).toBe(true);
    expect(index.isAlive(true, 3)).toBe(true);
    expect(index.isAlive(true, 4)).toBe(false);
    expect(index.isAlive(true, 5)).toBe(false);
    expect(index.isAlive(true, 6)).toBe(false);
    expect(index.isAlive(true, 7)).toBe(false);
    expect(index.isAlive(true, 8)).toBe(false);
    expect(index.isAlive(false, 1)).toBe(false);
    expect(index.isAlive(false, 2)).toBe(false);
    expect(index.isAlive(false, 3)).toBe(true);
    expect(index.isAlive(false, 4)).toBe(false);
    expect(index.isAlive(false, 5)).toBe(false);
    expect(index.isAlive(false, 6)).toBe(false);
    expect(index.isAlive(false, 7)).toBe(false);
    expect(index.isAlive(false, 8)).toBe(false);
  });
});

describe("グリッドクラス", () => {
  it("", () => {
    // const g = new index.Grid();
    // console.log(g);
    const g = new index.Grid(1,2);
    expect(g.width).toBe(1);

  });
});

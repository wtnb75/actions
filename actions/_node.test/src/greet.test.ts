import { describe, expect, it } from "vitest";

import { greet } from "./greet";

describe("greet", () => {
  it("returns a greeting", () => {
    expect(greet("world")).toBe("hello, world");
  });
});

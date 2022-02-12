%lang starknet
%builtins range_check

const hello = 10000805121215  # 08, 05, 12, 12, 15.
const world = 10002315181204  # 23, 15, 18, 12, 04.

@view
func greeting() -> (number1 : felt, number2 : felt):
    return (hello, world)
end
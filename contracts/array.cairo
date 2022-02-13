%lang starknet
%builtins pedersen range_check

from starkware.cairo.common.alloc import alloc

@view
func read_array{range_check_ptr}(index : felt) -> (value : felt):
    let(ptr : felt*) = alloc()
    
    assert [ptr] = 1
    assert [ptr + 1] = 2
    assert [ptr + 2] = 3
    assert [ptr + 3] = 4

    let val = ptr[index]
    return (val)
end
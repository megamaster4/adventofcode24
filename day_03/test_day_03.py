from day_03.main import find_correct_sections, multiply_numbers, assign_do_dont, find_correct_sections_do_dont


def test_find_correct_sections():
    memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    correct_memory = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    found_memory = find_correct_sections(memory=memory)

    assert found_memory == correct_memory


def test_find_correct_sections_do_dont():
    memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    corrected_memory = ['mul(2,4)', 'mul(8,5)']
    found_memory = find_correct_sections_do_dont(memory=memory)
    assigned_memory = assign_do_dont(memory=found_memory)
    
    assert assigned_memory == corrected_memory



def test_multiply_correct_memory():
    correct_memory = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    result = sum([multiply_numbers(correct_memory=item) for item in correct_memory])
    assert result == 161
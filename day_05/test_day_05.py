from day_05.main import check_order, get_middle_sum, construct_page_order_dict, transform_input, set_correct_order


def test_check_order_day_05():
    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    correct = [['75', '47', '61', '53', '29'], ['97', '61', '53', '29', '13'], ['75', '29', '13']]

    page_ordering_rules, page_numbers = transform_input(example)
    numbers = construct_page_order_dict(page_ordering_rules)

    correct_rows = []
    for row in page_numbers:
        row_splitted = row.split(',')
        if check_order(row_splitted, numbers):
            correct_rows.append(row_splitted)

    middle_sum = get_middle_sum(correct_rows)
    assert correct == correct_rows
    assert middle_sum == 143


def test_set_correct_order_day_05():
    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    correct = ['75,47,61,53,29', '97,61,53,29,13', '75,29,13']

    page_ordering_rules, page_numbers = transform_input(example)
    numbers = construct_page_order_dict(page_ordering_rules)

    incorrect_rows = []
    for row in page_numbers:
        row_splitted = row.split(',')
        if not check_order(row_splitted, numbers):
            incorrect_rows.append(row)
    
    correct_rows = []
    for row in incorrect_rows:
        incorrect = row.split(',')
        correct_rows.append(set_correct_order(incorrect, numbers))

    middle_sum = get_middle_sum(correct_rows)
    assert middle_sum == 123


    
        



from game_parser import parse
import cells

def test_parse():
    # simple parse
    simple= ['*X*', 'Y**']
    ins_tp = []
    for i, line in enumerate(simple):
            for j, char in enumerate(line):
                ins_tp.append(type(parse(simple)[i][j]))
    expected = [cells.Wall, cells.Start, cells.Wall, cells.End, cells.Wall, cells.Wall]
    actual = ins_tp
    assert actual == expected,'Simple_parse: failed'
    print('Simple parse: passed!')

    # parse with bad letter
    bad_letter = ['*b*', 'Y**']
    expected = ValueError('Bad letter in configuration file: b.')
    fail_message = 'Bad letter in configuration file: b.'
    try:
        actual = parse(bad_letter)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print('Bad letter: passed!')
    except Exception:
        print(fail_message)

    # parse with no x
    no_x = ['***', 'Y**']
    expected = ValueError('Expected 1 starting position, got 0.')
    fail_message = 'Expected 1 starting position, got 0.'
    try:
        actual = parse(no_x)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print('No x: passed!')
    except Exception:
        print(fail_message)

    # parse with too many x
    too_many_x = ['*XX', 'Y**']
    expected = ValueError('Expected 1 starting position, got 2.')
    fail_message = 'Expected 1 starting position, got 2.'
    try:
        actual = parse(too_many_x)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print('Too many x: passed!')
    except Exception:
        print(fail_message)

    # parse with no y
    no_y = ['*X*', '*W*']
    expected = ValueError('Expected 1 ending position, got 0.')
    fail_message = 'Expected 1 ending position, got 0.'
    try:
        actual = parse(no_y)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print('No Y: passed!')
    except Exception:
        print(fail_message)

    # parse with too many y
    too_many_y = ['*X*','YY*']
    expected = ValueError('Expected 1 ending position, got 2.')
    fail_message = 'Expected 1 ending position, got 2.'
    try:
        actual = parse(too_many_y)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print('Too many y: passed!')
    except Exception:
        print(fail_message)

    # parse with simple teleport
    simple_tele= ['X1*', 'Y*1']
    tele_map = []
    for i, line in enumerate(simple_tele):
            for j, char in enumerate(line):
                tele_map.append(type(parse(simple_tele)[i][j]))
    expected = [cells.Start, cells.Teleport, cells.Wall, cells.End, cells.Wall, cells.Teleport]
    actual = tele_map
    assert actual == expected,'Simple_tele: failed'
    print('Simple teleport: passed!')

    # parse with no matching teleport
    no_matching_tele = ['X1*', 'Y**']
    expected = ValueError('Teleport pad 1 does not have an exclusively matching pad.')
    fail_message = 'Teleport pad 1 does not have an exclusively matching pad.'
    try:
        actual = parse(no_matching_tele)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print('No matching teleport: passed!')
    except Exception:
        print(fail_message)

def run_tests():
    test_parse()


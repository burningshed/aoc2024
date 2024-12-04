
class Example:
    """Used to define custom examples for use with tester class
    """
    def __init__(self, input_data, answer_a, answer_b):
        """Define instance of custom example class. Use in a list.

        Args:
            input_data (_type_): custom input for example
            answer_a (_type_): expected answer for part a using input data
            answer_b (_type_): expected answer for part b using input data
        """
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.input_data = input_data
    
    def __repr__(self) -> str:
        return f"Input: \n{self.input_data}\n Answer A: {self.answer_a}\n Answer B: {self.answer_b}"

def tester(solver, part, puz, custom_examples=None, debug_mode=False):
    """Tests code for Advent of Code

    Args:
        solver (function): Function to be tested
        part (char): part of puzzle function is for - 'a' or 'b'
        puz (puzzle): puzzle provided by aocd, should provide input_data and examples
        custom_examples (list of Example objects, optional): list of examples if puz examples are not working/sufficient. should provide input_data, answer_a and answer_b for each. Defaults to None.
        debug_mode (bool, optional): Used to stop code from executing on puzzle data, where examples may work but code incomplete. Defaults to False.

    Returns:
        bool: True if found a possible answer, false otherwise
    """
    print(f"Testing part {part}")
    
    if custom_examples == None:
        examples = puz.examples
    else:
        examples = custom_examples
    # Define Example Data Location from Puzzle
    def get_answer(cur_example, cur_part):
        if cur_part == 'a':
            return cur_example.answer_a
        if cur_part == 'b':
            return cur_example.answer_b
            
    # Run through each example
    num = 1
    for example in examples:
        print(f"~~~~~~ Example {num} ~~~~~~~\n")
        print(example)
        print("")
        e_data = example.input_data
        e_answer = get_answer(example, part)
        if e_answer == None:
            num += 1
            print(f"Example has no answer for part {part}")
            continue
        try:
            ans = solver(e_data)
        except Exception as e:
            # Turn on debug mode if exception thrown
            debug_mode = True
            print("Error!")
            print(e)
            num += 1
            continue
        if ans != e_answer:
            # Turn on debug mode if output doesn't match
            debug_mode = True
            print("Incorrect Output!")
            print(f"Expected: {e_answer}\n\n Solver Output: {ans}\n")
        else:
            print("Example Passed!")
        num += 1
        print("")
        
    # run code on real input if debug mode not set
    if not debug_mode:
        print("Running Real Input")
        try:
            ans = solver(puz.input_data)
            print(ans)
            return True
        except Exception as e:
            print("Error!")
            print(e)
    return False
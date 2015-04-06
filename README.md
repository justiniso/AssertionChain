assertionchain
=============

An AssertionChain is a wrapper for a group of commands that must happen in sequence.

Features:

- Control order of execution of a group of functions
- Terminate execution of the rest of the chain if certain conditions are not met

Simple example:

    AssertionChain()\
        .do(lambda: 1 + 1, 'Add two numbers together') \
        .expect(3, message='Step "{step}" did not result in expected value {expected}, value was: {actual}') \
        .perform()

This is roughly equivalent to:

    val = 1 + 1
    assert val == 3

The above example is certainly more readable, so why use an AssertionChain at all? For starters, the chain
encourages the user to provide line-by-line detail about each step being executed. So if you want to understand
why the above assertion failed, you would have to explain where that value came from in the assertion, which can be
tedious. AssertionChain provides an API for performing incremental checks on the operations being executed in the
chain.

It is a simple utility for grouping related actions and ensuring each step succeeds. For instance, assume we have a
suite of functions that interact with files (get_contents, write_contents, delete_file). Their contract stipulates
that each function will return True of False depending on whether or not they were successful. We can use an
AssertionChain to make sure each step was successful:

    filename = '/tmp/sd9x0c2'
    new_contents = 'myfile'

    # Write the file, retrieve the contents
    contents = AssertionChain()\
        .do(lambda: get_contents(filename), 'Retrieve file contents').expect(None, operator='is not')\
        .do(lambda: write_contents(filename, new_contents), 'Write file content').expect(True, operator='is')\
        .do(lambda: write_contents(filename, ''), 'Write empty file content').expect(True, operator='is')\
        .perform()

    # Delete the file
    AssertionChain().do(lambda: delete_file(filename), 'Delete file').expect(True, operator='is').perform()

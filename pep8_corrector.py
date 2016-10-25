"""
Remove common PEP8 errors
- remove whitespaces from blankline
- make a new line at the end of file if it does not already exist
- remove trailing whitespaces
- ensure there are 2 new lines above functions
"""

# imports
import time

# Flags for the file
# (You can combine multiple flags together)
#
# 'o' - overwrite file (FILENAME will be directly modified)
FLAGS = ''

# define file that needs to be cleaned and an empty new file
# REQ: FILENAME exists in the same dir as pep8_corrector.py
# REQ: NEW_FILENAME exists in the same dir as pep8_corrector.py if no 'o' flag
# Note: NEW_FILENAME will be overwritten and existing text will be deleted.
FILENAME = "test.py"
NEW_FILENAME = "test2.py"

# if user wants to overwrite
if 'o' in FLAGS:
    unclean_file = open(FILENAME, "r+")
    
# user does not want to overwrite
else:
    
    # open a file for reading and a separate one for writing
    unclean_file = open(FILENAME, "r")
    new_file = open(NEW_FILENAME, "w")    


def remove_whitespace_from_blankline(unclean_element):
    """ (str) -> str
    Given an unclean string, remove whitespace in blank line and return the
    cleaned element
    """

    # create a blank lines corrected counter
    blank_lines_corrected = 0
    
    # create copy of unclean_element to cleaned_element
    cleaned_element = unclean_element

    # check if element is blank
    if unclean_element.strip() == '':

        # make next_line a newline character
        cleaned_element = '\n'
        blank_lines_corrected += 1
        
    # return cleaned line
    return cleaned_element


def make_new_line_at_end_of_file(unclean_file_list):
    """ (list) -> NoneType
    Given an unclean file's list, add a new newline element to end of list
    if it does not already exist. (mutate the list)
    """

    # search for the last element and check if it ends with a newline
    # character
    if (unclean_file_list[len(unclean_file_list) - 1].endswith('\n')):

        # append a newline element to the unclean_file_list
        unclean_file_list.append('\n')
        
        # print a message to show a newline has been made at end of file
        print('A new line has been made at the end of file')


def remove_trailing_whitespace(unclean_element):
    """ (str) -> str
    Given an unclean string, remove all the trailing whitespaces from all
    lines and return the cleaned string
    """

    # create counter to track trailing whitespace corrected
    trailing_whitespace_corrected = 0
    
    # shorten unclean_element
    element = unclean_element

    # right strip the right blankspace characters
    # note that elements are like this: 'hello \n'
    # so rstrip cannot do good right now

    # if there is trailing whitespace
    if ((element[len(element) - 2:len(element)] == ' \n') or
       (element[len(element) - 2:len(element)] == '\t\n')):

        # strip the right blankspace characters and add back newline
        # character
        #
        # Note: element = element.rstrip() doesn't allow the
        # list to mutate... interesting.
        cleaned_element = element.rstrip() + '\n'

    # if last character is not a newline character
    else:

        # right strip all whitespace characters
        cleaned_element = unclean_element.rstrip('\t ')
        
    # returned the cleaned string
    return cleaned_element


def two_lines_above_functions(unclean_file_list):
    """ (list) -> NoneType
    Given an unclean file's list, check if there are two newlines above it. If
    there are no two newline elements above it, then add the appropriate number
    of newline elements above it.

    Exception: If the line above is a comment, then start counting above the
    comment.
    Exception: If the function starts on the first line, then this rule does
    not apply.

    REQ: unclean_file_list does not have blankline element with whitespace

    """
    # loop through every element starting from index 1 in unclean_file_list
    for i in range(1, len(unclean_file_list)):

        # if the element starts with def
        if unclean_file_list[i].startswith('def'):

            # check with number of elements above
            no_of_elements_above = 1

            # look at the element above it
            element_above = unclean_file_list[i - no_of_elements_above]

            # loop this forever until a line has been found that is not a
            # comment
            while element_above.startswith('#'):

                # set element above to something higher
                no_of_elements_above += 1
                element_above = unclean_file_list[i - no_of_elements_above]

            # CASE 1: if element_above is not a blank line
            if element_above != '\n':

                # insert 2 blanklines after [i - no_of_elements]
                unclean_file_list.insert(i - no_of_elements, '\n')
                unclean_file_list.insert(i - no_of_elements, '\n')

            # CASE 2: if element_above is a blank line
            else:

                # let element_above be the line above it
                no_of_elements_above += 1
                element_above = unclean_file_list[i - no_of_elements_above]

                # if element_above is not a new line
                if (element_above != '\n'):

                    # insert a blankline after [i - no_of_elements_above + 1]
                    # + 1 because we want to insert after element_above
                    unclean_file_list.insert(i - no_of_elements_above + 1,
                                             '\n')


def one_space_after_hash_comment(unclean_element):
    """ (str) -> str
    Given an unclean element, if the line is a comment (starts with #), check
    if there is a space after the #. If not, then add the space and return the
    cleaned element. Else, return the element.
    """
    
    # if line starts with #
    if unclean_element.lstrip().startswith('#'):
        
        # if the character preceeding # is not a space
        if unclean_element.lstrip()[1] != ' ':
            
            # add a space after the # by string split
            cleaned_element = unclean_element[0] + " " + \
                unclean_element[1:]

        # if character preceeding # is a space
        else:
            
            # unclean_element is already clean
            cleaned_element = unclean_element
        
    # return the cleaned_element
    return cleaned_element

def main():
    """ () -> NoneType
    Run functions to make file with less PEP8 errors
    """

    # message to show what file is being processed
    print("Reading", FILENAME)

    # create a list for each line in file
    file_list = unclean_file.readlines()
    
    # starting to run PEP8 compliance functions
    print("\n\n### Running functions...")
    
    # loop through all the elements of file_list to run
    # functions that require inspection of every line
    for i in range(0, len(file_list)):    
        
        # Remove whitespace from blankline
        file_list[i] = remove_whitespace_from_blankline(file_list[i])
        
        # strip all trailing whitespaces
        file_list[i] = remove_trailing_whitespace(file_list[i])        
    
    # Run functions that does not require inspection of every
    # line.
    
    # Make new line at end of file if it doesn't exist
    make_new_line_at_end_of_file(file_list)

    # two blank lines above a function
    two_lines_above_functions(file_list)

    # loop through each element to write to the new file.
    for next_element in file_list:

        # if settings set to overwrite file
        if 'o' in FLAGS:
            unclean_file.write(next_element)

        # if settings set to not overwrite file
        else:
            new_file.write(next_element)

# start time of this script
start_time = time.time()

# run the main fucntion
main()

# calculate the time used to run the script
end_time = time.time()
time = round(end_time - start_time, 5)

# show some successful messages
if 'o' in FLAGS:
    print("\nSuccessfully formatted", FILENAME, "in", time, "seconds")
else:
    print("\nSuccessfully created new formatted file",
          NEW_FILENAME, "in", time, "seconds")

# closes the 2 files
unclean_file.close()
new_file.close()

# debugging
if (__name__ == "__main__"):

    # doctests
    import doctest
    doctest.testmod()

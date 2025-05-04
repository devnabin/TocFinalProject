'''
Project Name: PDA-Based HTML/XML Validator 
Theory of Computation (CSC720) 
Class Project
'''

# import re module to use regular expressions
import re

# import os module to interact with the operating system for file handling
import os


# function to extracts all tags from the HTML or XML string
def tokenizeTags(html):
    # extracting the valid html/xml tags using regex pattern matching
    # matches opening tags (e.g., <div>), closing tags (e.g., </div>), and self-closing tags (e.g., <img/>)
    tags = re.findall(r'</?[a-zA-Z][a-zA-Z0-9\-]*[^<>]*?/?>', html)
    
    # filter out xml declarations (e.g., <?xml...>) and doctype declarations (e.g., <!doctype>)
    filteredTags = [tag for tag in tags if not (tag.startswith('<?') or tag.startswith('<!'))]
    
    # Check if no valid tags are found (e.g., input is plain text like "hello")
    if not filteredTags:
        raise ValueError("Error: no valid tags found in the input.")
    
    # remove all valid tags from input to check for stray '<' or '>' characters
    stripped = re.sub(r'<[^>]+>', '', html)  # leaves only non-tag content
    
    # checking if there are unmatched '<' or '>' in remaining content (e.g., "<div" without '>' or "hello>world")
    if '<' in stripped or '>' in stripped:
        raise ValueError("Error: unmatched '<' or '>' found outside of tags.")
    
    # returning list of filtered tags for structural validation
    return filteredTags


# this function identifies the type and name of each tag
def extractTagName(tag):
    
    # check if it is a closing tag
    if tag.startswith('</'):
        return 'CLOSE', tag[2:].split()[0].rstrip('>')
    
    # check if it is a self-closing tag
    elif tag.endswith('/>') or tag[-2:] == '/>':
        return 'SELFCLOSE', tag[1:].split()[0]
    
    # otherwise, treat it as an opening tag
    else:
        return 'OPEN', tag[1:].split()[0].rstrip('>')



# defining a set of known self-closing tags in HTML
selfClosingTags= {
    'img', 'br', 'input', 'meta', 'link', 'hr', 'col', 'area',
    'base', 'embed', 'param', 'source', 'track', 'wbr'
}


# this function checks if tags follow proper nesting using PDA stack logic
def isWellFormed(tokens):
    
    # initialize an empty stack
    stack = []

    # go through each tag
    for i, tag in enumerate(tokens):
    
        # extract tag type and tag name
        tagType, tagName = extractTagName(tag)
        
        # make tag name lowercase for case-insensitive conditions
        tagName = tagName.lower() 

        # if it's an opening tag, push it to the stack
        if tagType == 'OPEN':
            stack.append(tagName)

        # if it's a closing tag, check if it matches with the last opened tag
        elif tagType == 'CLOSE':
            
            # checking for self-closing tags which should not have closing tag
            if tagName in selfClosingTags:
                print(f"error at tag {i + 1}: </{tagName}> is a self-closing tag and cannot have a closing tag.")
                return False
            
            # if stack is empty to check if there's no opening tag to match
            if not stack:
                print(f"error at tag {i + 1}: unexpected closing tag </{tagName}> while stack is empty")
                return False
            
            # if the closing tag doesn't match the last opened tag then it can be say invalid
            if stack[-1] != tagName:
                print(f"error at tag {i + 1}: closing tag </{tagName}> does not match opening tag <{stack[-1]}>")
                return False
            
            # if it matches then pop the tag from the stack
            stack.pop()

        # self-closing tags do not affect the stack

    # after processing all tags
    # checking stack because it should be empty for valid structure
    if stack:
        print(f"Error: unclosed tags keep remain on stack: {stack}")
        return False

    # if everything matched properly then return True
    return True


# this function reads the content of a file
def readFromFile(filename):
    
    # check if the file exists on the same path or directory
    if not os.path.exists(filename):
        print(f"Error: file '{filename}' not found, please check file and try agin.")
        return None
    
    # open the file and then read its content
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


# this function for interactive PDA validator
def runValidator():
    
    # show command instructions to the user for their ease
    print("html/xml validator using pda")
    print("commands:")
    print("  validate <filename> - validate html or xml file content")
    print("  read <filename>     - display file content")
    print("  <html>...</html>    - you can also paste html directly")
    print("  exit                - quit the program")

    # taking input
    while True:
        print('\n')
    
        # read user input
        userInput = input("Enter HTML/XML: ").strip()

        # exit or terminate the program when user types 'exit' and then it will stop the loop
        if userInput.lower() == 'exit':
            print("Thank you, for using PDA-Based HTML/XML Validator.")
            break

        # program for 'validate <filename>' command
        if userInput.lower().startswith("validate "):
            filename = userInput[9:].strip()
            html = readFromFile(filename)
            
            # continue if file not found
            if html is None:
                continue
            
            # validate the html/xml structure
            try:
                
                # tokenize the html/xml content
                tokens = tokenizeTags(html)
                
                # print validation result
                if isWellFormed(tokens):
                    print("Good! This is a valid html/xml structure.")
                else:
                    print("Error! invalid or mismatched tags.")
            
            
            except ValueError as e:
                print(f"validation error: {e}")
                print("Sad! invalid html/xml structure.")

        # implementing 'read <filename>' to show content of the file
        elif userInput.lower().startswith("read "):
            filename = userInput[5:].strip()
            
            # read the file content
            content = readFromFile(filename)
            
            # if content is not None then print the content
            if content is not None:
                print(f"\ncontent of '{filename}':")
                print(content)
                print()

        # taking direct html/xml input from user
        else:
            html = userInput
            try:
                # tokenize the html/xml content
                tokens = tokenizeTags(html)
                if isWellFormed(tokens):
                    print("Good! This is a valid html/xml structure.")
                else:
                    print("Error! This is a invalid or mismatched tags.")
                    
            except ValueError as e:
                print(f"validation error: {e}")
                print("invalid html/xml structure.")

# start the validator program
runValidator()
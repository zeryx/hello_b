import Algorithmia

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
    return "hello {} from org B, we've pushed a new release. Hey Jaime look at this!".format(input)

class GCgate:
    """
    a set of bijection function (gates) for the GC coloring stuff
    extremely skeletal for now
    """
    def __init__(self,A ,k, l, function, name):
        """Initiates a new gate.
            Arguements: 
                - function: blackbox
                - name: just a name :)
                - A: alphabet
                - k: input length
                - l: output length
        """
        self.input = x
        self.name = name
        self.gate = function
        self.output = list()

        if not self.check_input():
            raise ValueError('Invalid input')
        if not self.check_function():
            raise ValueError('Invalid gate function')

        # self.output = function(x)
        
    
    def check_input(self):
        """
        helper function no.1
        check if input is valid, should check length & alphabet
        should be a list of length 2, each element in the list should be a quadruple (?)
        return True if input is valid, False otherwise
        """
        return False

    def check_function(self):
        """
        helper function no.2
        check if the gate function is valid (how to identify?) 
        return True if function is valid, False otherwise
        """
        return False

    def evaluate(self, x):
        return 

    ## a dictionary for the elements in C <- conjugacy class
    ## propably later, need to look at sage data structure first D:
    c_class = {
    }

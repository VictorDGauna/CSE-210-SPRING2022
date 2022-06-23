


from click import prompt


class TerminalService:


    def read_letter(self, prompt):
        
        return input(prompt)

    def write_letter(self, letter):
        
        print(letter)
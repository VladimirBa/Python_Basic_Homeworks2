class Editor:

    @staticmethod
    def view_document():
        print('You may only view your text in the free version of the Text Editor Pro.')

    @staticmethod
    def edit_document():
        print('You have to pay to edit your text in the Text Editor Pro.')


class ProEditor:

    @staticmethod
    def edit_document(lic_key):
        while lic_key != '1357':
            parent_class_obj = Editor()
            parent_class_obj.edit_document()
            return "Sorry. You have entered an incorrect license code."
        else:
            ProEditor()
            return 'You are permitted to edit your text!'


start = Editor()
start.view_document()
start.edit_document()
text = ProEditor()
lk = input('Please, enter the license code you received by email after payment: ')
print(text.edit_document(lic_key=lk))

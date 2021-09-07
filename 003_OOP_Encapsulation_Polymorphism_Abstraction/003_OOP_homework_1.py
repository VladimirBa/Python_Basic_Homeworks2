class Editor:

    def view_document(self):
        print('You may only view your text in the free version of the Text Editor Pro.')

    def edit_document(self):
        print('You have to pay to edit your text in the Text Editor Pro.')


class ProEditor(Editor):

    def edit_document(self):
        print('You are permitted to edit your text!')


def main():
    editor = Editor()
    editor.view_document()
    editor.edit_document()
    proeditor = ProEditor()

    lk = input('Please, enter the license code you received by email after payment: ')
    if lk == '1357':
        proeditor.edit_document()
    else:
        print("Sorry. You have entered an incorrect license code.")


if __name__ == '__main__':
    main()

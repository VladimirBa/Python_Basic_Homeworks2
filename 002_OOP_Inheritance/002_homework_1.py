class Editor:

    def view_document(self):
        pass

    def edit_document(self):
        return "You can't edit the files in free 'Document Viewer'. \nYou will receive access code after payment."


class ProEditor(Editor):

    # def __init__(self, access_code):
    #     self.access_code = access_code

    def edit_document(self, access_code):
        access_code = input('Enter access code you received by email: ')
        if access_code != '1357':
            super().edit_document(self, access_code)

doc = ProEditor()
print(doc.edit_document(access_code=''))
from lib2to3.refactor import get_all_fix_names


class UserForms:
    def write_form_on_file(self, form: str):
        formsDataBase = open("./FormsDataBase.txt", "a", encoding="utf_8")
        formsDataBase.write(form + "\n")
        formsDataBase.close()

    def get_all_forms(self):
        allFormsFile = open("./FormsDataBase.txt", "r", encoding="utf_8")
        allForms = []

        while(True):
            line = allFormsFile.readline()

            if not line:
                break

            allForms.append(line)

        return allForms

    def get_all_forms_of_user(self, userId: int, isValidatingData: bool):
        forms = []
        formsDataBase = open("./FormsDataBase.txt", "r", encoding="utf_8")

        while True:
            line = formsDataBase.readline()

            if not line:
                break

            if(isValidatingData):
                startUserIdIndex = line.find("User: ") + 6
                
                if int(line[startUserIdIndex : len(line) - 1]) != userId:
                    continue

                forms.append(line[0 : startUserIdIndex - 7])
            
            elif(isValidatingData == False):
                forms.append(line)

        formsDataBase.close()

        return forms

    def get_form_index(self, form: str):
        allForms = self.get_all_forms()
        iteration = 0

        for i in allForms:
            if(i == form):
                return iteration

            iteration += 1

        return -1

    def delete_form_of_user(self, userId: int, formIndexLocal: int):
        userForms = self.get_all_forms_of_user(userId, False)
        formToDelete = userForms[formIndexLocal]
        allForms = self.get_all_forms()
        formIndexGlobal = self.get_form_index(formToDelete)

        allForms.pop(formIndexGlobal)

        formsFile = open("./FormsDataBase.txt", "w", encoding="utf_8")

        for i in allForms:
            formsFile.write(i)

class note:
    memo=None
    note_id=0
    all_notes=[]
    __all_notes_id__ = []
    def __init__(self):
        pass
    def new(self):
        self.memo = input("enter your text: ")
        self.note_id +=1
        self.all_notes.append(self.memo)
        self.__all_notes_id__.append(self.note_id)

    def search(self):
        self.flag = 0
        
        self.phrase = input("enter the phrase you want to search: ")
        for i in range(len(self.all_notes)+1):
            if self.phrase in self.all_notes[i]:
                self.flag = 1
                break
                
            else:
                self.flag=0

        if self.flag == 1:
            print("phrase found")

        else:
            print("phrase not found")
                
                


    def edit(self):
        print("which note do you want to edit?")
        print(self.all_notes)
        self.no = int(input("enter it's note_id :"))
        if self.no in self.__all_notes_id__:

            self.new= input("enter the new text you want to insert in place of the previous one : ") 
            self.all_notes.remove(self.all_notes[self.no-1])
            self.all_notes.insert(self.no-1,self.new)
            print("edited sucessfully!")
            # self.show=input("do you want to see the edited result? [y/n]")
            while True:
                self.show=input("do you want to see the edited result? [y/n]")
                if self.show.lower()=="y":
                    print(self.all_notes)
                    

                else:
                    print("enter the correct choice")

    def main(self):
        while True:
            try:self.task = int(input("enter your choice : "))
            except:
                print("please enter a integer!") 
            else:
                # self.task = int(input("enter your choice : "))
                if self.task == 1:
                    self.new()

                elif self.task == 2:
                    self.search()

                elif self.task == 3:
                    self.edit()

                elif self.task == 5:
                    break
        
            
print("1 : add new note \n 2 : search in the existing notes \n 3 : edit an existing note \n 5 : quit ")

a=note()
a.main()
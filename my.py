# a notebook type program where you can add notes and dp many things with them (like google notes)

class note:
    memo=None
    note_id=0
    all_notes=[]
    __all_notes_id__ = []

# initialization of the program

    def __init__(self):
        pass

# a function to add a new note
 
    def new(self):
        self.memo = input("enter your text: ")
        self.note_id +=1
        self.all_notes.append(self.memo)
        self.__all_notes_id__.append(self.note_id)

# a function to search inside the whole notebook, a feature to be added so that it will also pinpoint the location of the phrase inside the note

    def search(self):
        self.flag = 0
        self.pos=0
        
        self.phrase = input("enter the phrase you want to search: ")
        for i in range(len(self.all_notes)+1):
            if self.phrase in self.all_notes[i]:
                self.flag = 1
                self.pos=i
                break
                
            else:
                self.flag=0

        if self.flag == 1:
            print("phrase found")
            print(f"the phrase is inside the {self.all_notes[self.pos+1]} note")

        else:
            print("phrase not found")
                
                
# to edit the existing note like if we want to erase an existing note and add some other text in place of that

    def edit(self):
        print("which note do you want to edit?")
        print(self.all_notes)
        self.no = int(input("enter it's note_id :"))
        if self.no in self.__all_notes_id__:

            self.new2= input("enter the new text you want to insert in place of the previous one : ") 
            self.all_notes.remove(self.all_notes[self.no-1])
            self.all_notes.insert(self.no-1,self.new2)
            print("edited sucessfully!")
            # self.show=input("do you want to see the edited result? [y/n]")
            while True:
                self.show=input("do you want to see the edited result? [y/n]")
                if self.show.lower()=="y":
                    print(self.all_notes)
                    break
                elif self.show.lower()=="n":
                    break
            
                    

                else:
                    print("enter the correct choice")

# to append inside an existing note

    def edit_in(self):
        print("which note do you want to edit?")
        print(self.all_notes)
        try:
            self.no = int(input("enter it's note_id :"))
        except:
            print("enter the correct choice")
            # self.no = int(input("enter it's note_id :"))
        finally:
            if self.no in self.__all_notes_id__:

                self.new1= input("enter the text you want to insert : ") 
                self.all_notes[self.no - 1] = self.all_notes[self.no - 1] + " " + self.new1
                
            print("edited sucessfully!")
            # self.show=input("do you want to see the edited result? [y/n]")
            while True:
                self.show=input("do you want to see the edited result? [y/n]")
                if self.show.lower()=="y":
                    print(self.all_notes)
                    break
                elif self.show.lower()=="n":
                    break
            
                    

                else:
                    print("enter the correct choice")

# to see all the notes present in the notebook

    def show_all(self):
        print(self.all_notes)

# to merge 2 notes as of now, takes the input from the user which contains the position of the later note which will be merged with the previous one ( giving an error, seemingly " index out of the list range " type error)

    def merge(self):
        self.num = int(input("enter the note id of note you want to merge with the previous one: "))
        if self.num not in self.__all_notes_id__:
            print("not a valid note id !")
        else:
            self.all_notes[self.num - 1]+=" "+self.all_notes[self.num]
            self.all_notes.remove(self.all_notes[self.num])

#main function that will execute all the tasks

    def main(self):
        while True:
            try:self.task = int(input("enter your choice : "))
            except:
                print("please enter a integer!") 
            else:
                # self.task = int(input("enter your choice : "))
                if self.task == 1:
                    self.new()

                if len(self.all_notes)!=0:

                    if self.task == 2:
                        self.search()

                    elif self.task == 3:
                        self.edit()

                    elif self.task == 4:
                        self.edit_in()

                    elif self.task == 5:
                        self.show_all()

                    elif self.task == 6:
                        self.merge()

                else:
                    print("list is empty")

                if self.task == 7:
                        break
                
            
            
print(" 1 : add new note \n 2 : search in the existing notes \n 3 : edit an existing note \n 4 : edit in an existing note \n 5 : show all notes \n 6 : merge notes \n 7 : quit")

a=note()
a.main()
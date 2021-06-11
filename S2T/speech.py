import speech_recognition as sr

#defining rules
def ruleset():
    rules = {
            "General": {
                            "H T M L": "HTML",
                            "Triple A": "AAA",
                            "DOLLARS": "$",
                            "TWO DOLLARS": "$2"
            },

            
            
            "Numbers":{
                            "zero": 0,
                            "one" : 1,
                            "two": 2,
                            "three": 3,
                            "four": 4,
                            "five": 5,
                            "six": 6,
                            "seven": 7,
                            "eight": 8,
                            "nine": 9,
                            "ten": 10,
                            
                            },
            "Tuples": {
                            "single":1,
                            "double":2,
                            "triple":3,
                            
                        }
           
            }
    return rules

#checking if word has comma at front or at last or at both  if true then return front,word and last 
def check_front_last(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last


    #class for conversion
class SpokenToWritten:

    def __init__(self):

        self.rules=ruleset()
        self.paragraph=""
        self.ouptut_para=""

    #getting user input
    def get_user_input(self,paragraph):

        self.paragraph=paragraph

    #getting  user output
    def show_output(self):
        
        print("\nConverted Written English Paragraph: \n\n \"" +self.ouptut_para+"\"")


    #main conversion function of spoken to written english 
    def Convert(self):
        #splitting paragraph into individual words
        words_of_para=self.paragraph.split()

        #accessing defines rules
        numbers=self.rules['Numbers']
        tuples=self.rules['Tuples']
        general=self.rules['General']
        i=0
        no_of_words=len(words_of_para)
        #loop will run for the number of words in paragraph 
        while i<no_of_words: 
            
            front,word,last=check_front_last(words_of_para[i])
            #Word of paragraph may of form ',dollars.' 
            if i+1!= no_of_words:
            #when word is of the form e.g.: two 
                front_n,next_word,last_n=check_front_last(words_of_para[i+1])
                if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                    self.ouptut_para=self.ouptut_para+" "+front+"$"+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in tuples.keys() and len(next_word)==1:
                    #when word is of form Triple A
                    self.ouptut_para=self.ouptut_para+" "+front_n+(next_word*tuples[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in general.keys():
                    #if word is of form P M or C M
                    self.ouptut_para=self.ouptut_para+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                    i=i+1
            else:
                self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                i=i+1



def converter():


        try:
            text=input("[Enter necessary words]:")
            print("[This is what you told]: {} ".format(text))

        except:
            print('[ERROR]:Sorry I Coudnt recognize your voice')

        try:    
            obj_spoken=SpokenToWritten()
            obj_spoken.get_user_input(text)
            obj_spoken.Convert()
            obj_spoken.show_output()
        except:
            print('Couldnt convert')

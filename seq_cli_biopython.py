# Program to perform basic operations on DNA, RNA and Protein sequences using Biopython

from Bio.Seq import Seq # Importing the Seq class from Biopython

if __name__== '__main__' :
             # Displaying menu to the user
             choice1 = input ("What type of sequence do you want to use? Choose one of the following: \n 1 : DNA \n 2 : RNA \n 3 : Protein \n 4 : Quit \n Enter your choice: ")

            
             choice = int(choice1)


             if choice == 1 : # DNA operations
                 
                 sequence = input("Enter the DNA sequence : ")
                 print("Operations available for this type of sequence are : ")
                 print("1 : Complement")
                 print("2 : Transcription")
                 print("3 : Quit")
                 choice = int(input("Enter the number of your choice : "))

                 if choice == 1: # Complement
                     dna = Seq(sequence)
                     comp = dna.complement()
                     print("The complement sequence is : ",  comp)

                 elif choice == 2 : # Transcription
                     dna = Seq (sequence)
                     transcribed_dna = dna.transcribe()
                     print("The resulting RNA (transcribed DNA) is : ", transcribed_dna)

                 elif choice == 3: # Quit
                     print("See you soon")
                 else : 
                     print("Invalid choice")
        
             elif choice == 2 : # RNA operations
                  
                  sequence = input("Enter the RNA sequence : ")
                  print ("Operations available for this type of sequence are : ")
                  print ("1 : Translation")
                  print ("2 : Quit")
                  choice = int(input("Enter the number of your choice : "))

                  if choice == 1: # Translation

                    if (len(sequence)%3!=0): # Invalid reading frame length
                     print("ERROR IN READING FRAME!")

                    else: # Valid reading frame length
                     arn = Seq(sequence)
                     translated = arn.translate()
                     print("The protein sequence obtained is : ", translated)

                  elif choice == 2: # Quit
                     print("See you soon.")
                  else : 
                     print("Invalid choice.") 
                      
             elif choice == 3: # Protein operations
                 print("No operations available for this type of sequences.")

             elif choice == 4 : # Quit
                 print("See you soon.")

             else: 
                print("Invalid Choice.")
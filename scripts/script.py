import random

def generate_random_amino_acids():
    '''
    הפונקציה מחזירה רשימה של חומצות אמינו אקראי באורך 149 תווים, כאשר החלוקה היא:
    50% חומצות אמינו לא קוטביות
    30% חומצות אמינו קוטביות
    10% חומצות אמינו טעונות חיובי
    10% חומצות אמינו טעונות שלילי
    '''
    amino_acids_seq_list = []

    NonPolar = ['A', 'V', 'L', 'I', 'P', 'F', 'M', 'W', 'G', 'C'] #50%
    for i in range (int(150*0.5-1)):
        amino_acids_seq_list.append(random.choice(NonPolar))
    Polar = ['N', 'Q', 'S', 'T', 'Y'] #30%
    for i in range (int(150*0.3)):
        amino_acids_seq_list.append(random.choice(Polar))
    PositivelyCharged = ['K', 'R', 'H'] #10%
    for i in range (int(150*0.1)):
        amino_acids_seq_list.append(random.choice(PositivelyCharged))
    NegativelyCharged = ['D', 'E'] #10%
    for i in range (int(150*0.1)):
        amino_acids_seq_list.append(random.choice(NegativelyCharged))

    random.shuffle(amino_acids_seq_list)
    return amino_acids_seq_list 

# תוכנית ראשית
num_seq = int(input("Please indicate how many random protein sequences you need (1-1000)?"))
# בדיקת קלט שאינו תקין
while (num_seq < 1 or num_seq > 1000):
    print("Invalid input. Please enter a number between 1 and 1000.")
    num_seq = int(input("Please indicate how many random protein sequences you need (1-1000)?"))

#פתיחת קובץ תוצאות
RandProtSeq = open('results/Out_RandProtSeq.txt', 'w')

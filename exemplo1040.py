def main():
    N = float(input()).split()
    N1 = N[0]
    N2 = N[1]
    N3 = N[2]
    N4 = N[3]

    average = ((2 * N1) + (3 * N2) + (4 * N3) + (N4))/10

    if average > 7.0:
        print("Aluno aprovado.")
    if average < 5.0:
        print("Aluno reprovado.")
    
    
    else:
        print("Aluno em exame.")
        continue
            new_media = one_more_score + average)/2
            if new_media/2 > 5.0:
                print("Aluno aprovado.")
                continue
                print("Aluno reprovado.")
                print("Media final: " + str(new_media))
            
        print("Nota do exame: " + )

if __name__ == "__main__":
    main()
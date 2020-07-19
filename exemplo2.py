def main():
   entrada = int(input())
   hora = entrada/3600
   minuto = (entrada%3600)/60
   segundo = (entrada%3600)%60
   print (str(int(hora)) + ":" + str(int(minuto)) + ":" + str(int(segundo)))  


if __name__ == "__main__":
    main()